#include <WiFi.h>
#include <DHT.h>
#include <ThingSpeak.h>
#include "secrets.h"

#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);
WiFiClient client;
unsigned long lastUpload = 0;
const unsigned long uploadInterval = 20000;

void connectWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print('.');
  }
  Serial.println(" connected");
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  connectWiFi();
  ThingSpeak.begin(client);
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) connectWiFi();
  if (millis() - lastUpload < uploadInterval) { delay(100); return; }
  lastUpload = millis();

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("DHT11 read failed");
    return;
  }

  ThingSpeak.setField(1, temperature);
  ThingSpeak.setField(2, humidity);
  int status = ThingSpeak.writeFields(THINGSPEAK_CHANNEL_ID, THINGSPEAK_API_KEY);
  Serial.printf("Temperature: %.1f C | Humidity: %.1f %% | ThingSpeak: %d\n",
                temperature, humidity, status);
}
