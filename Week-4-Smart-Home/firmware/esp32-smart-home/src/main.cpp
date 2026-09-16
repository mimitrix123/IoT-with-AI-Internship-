#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoOTA.h>

// Reference firmware: replace credentials/configuration with a private config.h.
// Sensors are intentionally represented by GPIO reads so the project can be adapted
// to DHT22/DS18B20, PIR/mmWave, LDR and sound sensors.

static const int TEMP_PIN = 34;
static const int MOTION_PIN = 27;
static const int LIGHT_PIN = 35;
static const int SOUND_PIN = 32;
static const int STATUS_LED = 2;

WiFiClient net;
PubSubClient mqtt(net);

volatile int temperatureRaw = 0;
volatile int lightRaw = 0;
volatile int soundRaw = 0;
volatile bool motion = false;

void readSensors(void *) {
  for (;;) {
    temperatureRaw = analogRead(TEMP_PIN);
    lightRaw = analogRead(LIGHT_PIN);
    soundRaw = analogRead(SOUND_PIN);
    motion = digitalRead(MOTION_PIN) == HIGH;
    vTaskDelay(pdMS_TO_TICKS(1000));
  }
}

void publishTelemetry(void *) {
  for (;;) {
    if (WiFi.status() == WL_CONNECTED && mqtt.connected()) {
      char payload[256];
      snprintf(payload, sizeof(payload),
        "{\"temperature_raw\":%d,\"motion\":%s,\"light_raw\":%d,\"sound_raw\":%d,\"uptime_s\":%lu}",
        temperatureRaw, motion ? "true" : "false", lightRaw, soundRaw, millis() / 1000UL);
      mqtt.publish("home/room1/telemetry", payload, true);
    }
    vTaskDelay(pdMS_TO_TICKS(5000));
  }
}

void maintainMqtt(void *) {
  for (;;) {
    if (WiFi.status() == WL_CONNECTED && !mqtt.connected()) {
      // Configure broker authentication in private config.h for a real deployment.
      mqtt.connect("esp32-smart-home");
    }
    mqtt.loop();
    vTaskDelay(pdMS_TO_TICKS(100));
  }
}

void setup() {
  pinMode(MOTION_PIN, INPUT);
  pinMode(STATUS_LED, OUTPUT);
  digitalWrite(STATUS_LED, LOW);
  Serial.begin(115200);

  // Replace with private credentials before deployment.
  WiFi.begin("YOUR_WIFI_SSID", "YOUR_WIFI_PASSWORD");
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    digitalWrite(STATUS_LED, !digitalRead(STATUS_LED));
  }

  mqtt.setServer("YOUR_MQTT_BROKER", 1883);
  ArduinoOTA.setHostname("esp32-smart-home");
  ArduinoOTA.begin();

  xTaskCreatePinnedToCore(readSensors, "Sensors", 4096, nullptr, 2, nullptr, 1);
  xTaskCreatePinnedToCore(publishTelemetry, "Telemetry", 4096, nullptr, 1, nullptr, 1);
  xTaskCreatePinnedToCore(maintainMqtt, "MQTT", 4096, nullptr, 1, nullptr, 0);
}

void loop() {
  ArduinoOTA.handle();
  delay(10);
}
