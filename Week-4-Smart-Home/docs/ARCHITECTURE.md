# System Architecture

```text
+---------------- ESP32 ----------------+
| Temp | Motion | Light | Sound         |
|       FreeRTOS sensor + MQTT tasks    |
+------------------+--------------------+
                   | MQTT/TLS
                   v
+------------- Raspberry Pi -------------+
| Broker/client | validation | storage   |
| occupancy AI  | energy AI  | automation |
+-------+------------+-----------+--------+
        |            |           |
   Dashboard     Voice API   Notifications

                   |
             Optional actuators
```

## Responsibilities
- **ESP32:** acquire sensors, timestamp data, maintain connectivity, perform lightweight local rules and OTA maintenance.
- **Raspberry Pi:** gateway, authenticated command validation, AI inference, dashboard backend, notification dispatch and local storage.
- **AI:** occupancy classification and energy recommendations using historical sensor/device data.
- **Clients:** dashboard, voice interface and mobile notification channel.

## Reliability
- Safe state on boot and communication failure.
- Bounded actuator commands and rate limits.
- Local fallback rules when AI or network services are unavailable.
- Watchdog and service supervision on edge devices.
