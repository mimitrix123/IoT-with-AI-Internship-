# Deep sleep strategy

For battery operation, wake the ESP32 on a timer, sample sensors, publish telemetry, perform any required irrigation decision, then enter deep sleep again.

```cpp
esp_sleep_enable_timer_wakeup(SLEEP_SECONDS * 1000000ULL);
esp_deep_sleep_start();
```

Important: MQTT/Wi-Fi connections do not survive deep sleep. Reconnect after every wake cycle. If continuous OTA availability is required, use a powered/active mode rather than deep sleep during the maintenance window.
