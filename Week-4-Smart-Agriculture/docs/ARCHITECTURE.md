# System architecture

The ESP32 is the edge controller. FreeRTOS separates sensor acquisition, irrigation control, OLED rendering and MQTT communication. Telemetry is published to a broker/cloud service. An AI model can use historical sensor data to recommend irrigation, while a deterministic soil threshold and maximum pump runtime remain as safety controls.

## Data path

Sensors -> ADC/digital inputs -> ESP32 -> MQTT -> cloud/dashboard -> historical dataset -> AI model -> recommendation.

## Reliability
- Default pump OFF on boot.
- Limit pump activation duration.
- Validate MQTT commands.
- Handle Wi-Fi/MQTT reconnection.
- Keep credentials outside source control.
- Calibrate soil thresholds for the actual crop, soil and sensor.
