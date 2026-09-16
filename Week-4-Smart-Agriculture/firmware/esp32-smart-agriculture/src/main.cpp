#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ArduinoOTA.h>

// Replace these with local configuration; never commit real credentials.
#include "config.h"

constexpr uint8_t SOIL_PIN = 34;
constexpr uint8_t TEMP_PIN = 35; // Connect an analog temperature sensor or adapt for your sensor.
constexpr uint8_t LIGHT_PIN = 32;
constexpr uint8_t RELAY_PIN = 26;
constexpr uint8_t OLED_ADDR = 0x3C;
constexpr uint8_t OLED_W = 128;
constexpr uint8_t OLED_H = 64;
constexpr uint32_t SAMPLE_MS = 5000;
constexpr uint32_t MAX_PUMP_MS = 15000;

Adafruit_SSD1306 display(OLED_W, OLED_H, &Wire, -1);
WiFiClient wifiClient;
PubSubClient mqtt(wifiClient);

struct SensorData { int soil; int tempRaw; int light; bool pump; };
SensorData data{};
SemaphoreHandle_t dataMutex;

int readSoil() { return analogRead(SOIL_PIN); }
int readLight() { return analogRead(LIGHT_PIN); }

void publishTelemetry() {
  if (!mqtt.connected()) return;
  char payload[192];
  SensorData snapshot;
  xSemaphoreTake(dataMutex, portMAX_DELAY);
  snapshot = data;
  xSemaphoreGive(dataMutex);
  snprintf(payload, sizeof(payload),
           "{\"soil_raw\":%d,\"temperature_raw\":%d,\"light_raw\":%d,\"pump\":%s}",
           snapshot.soil, snapshot.tempRaw, snapshot.light, snapshot.pump ? "true" : "false");
  mqtt.publish(MQTT_TOPIC_TELEMETRY, payload, true);
}

void sensorTask(void*) {
  for (;;) {
    SensorData next{readSoil(), analogRead(TEMP_PIN), readLight(), false};
    xSemaphoreTake(dataMutex, portMAX_DELAY);
    data.soil = next.soil;
    data.tempRaw = next.tempRaw;
    data.light = next.light;
    xSemaphoreGive(dataMutex);
    vTaskDelay(pdMS_TO_TICKS(SAMPLE_MS));
  }
}

void irrigationTask(void*) {
  for (;;) {
    int soil;
    xSemaphoreTake(dataMutex, portMAX_DELAY);
    soil = data.soil;
    xSemaphoreGive(dataMutex);

    // Conservative deterministic fallback. Calibrate threshold for the actual soil/sensor.
    bool dry = soil < SOIL_DRY_THRESHOLD;
    if (dry) {
      digitalWrite(RELAY_PIN, HIGH);
      xSemaphoreTake(dataMutex, portMAX_DELAY);
      data.pump = true;
      xSemaphoreGive(dataMutex);
      vTaskDelay(pdMS_TO_TICKS(MAX_PUMP_MS));
      digitalWrite(RELAY_PIN, LOW);
      xSemaphoreTake(dataMutex, portMAX_DELAY);
      data.pump = false;
      xSemaphoreGive(dataMutex);
    }
    vTaskDelay(pdMS_TO_TICKS(10000));
  }
}

void displayTask(void*) {
  for (;;) {
    SensorData snapshot;
    xSemaphoreTake(dataMutex, portMAX_DELAY);
    snapshot = data;
    xSemaphoreGive(dataMutex);
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(0, 0);
    display.printf("Smart Agriculture\nSoil: %d\nTemp raw: %d\nLight: %d\nPump: %s",
                   snapshot.soil, snapshot.tempRaw, snapshot.light, snapshot.pump ? "ON" : "OFF");
    display.display();
    vTaskDelay(pdMS_TO_TICKS(1000));
  }
}

void mqttTask(void*) {
  for (;;) {
    if (WiFi.status() == WL_CONNECTED) {
      if (!mqtt.connected()) mqtt.connect(MQTT_CLIENT_ID, MQTT_USER, MQTT_PASSWORD);
      mqtt.loop();
      publishTelemetry();
    }
    vTaskDelay(pdMS_TO_TICKS(10000));
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

  Wire.begin();
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) delay(300);

  mqtt.setServer(MQTT_HOST, MQTT_PORT);
  ArduinoOTA.setHostname(MQTT_CLIENT_ID);
  ArduinoOTA.begin();

  dataMutex = xSemaphoreCreateMutex();
  xTaskCreatePinnedToCore(sensorTask, "Sensors", 4096, nullptr, 2, nullptr, 1);
  xTaskCreatePinnedToCore(irrigationTask, "Irrigation", 4096, nullptr, 2, nullptr, 1);
  xTaskCreatePinnedToCore(displayTask, "OLED", 4096, nullptr, 1, nullptr, 0);
  xTaskCreatePinnedToCore(mqttTask, "MQTT", 4096, nullptr, 1, nullptr, 0);
}

void loop() {
  ArduinoOTA.handle();
  // A production battery profile should enter deep sleep after telemetry/irrigation cycles.
  delay(10);
}
