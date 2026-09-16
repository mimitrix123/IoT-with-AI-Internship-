# Week 4 — IoT Smart Agriculture + AI

Complete ESP32-based smart agriculture reference implementation.

## Scope
- Soil moisture, temperature and light sensing
- Automatic relay-controlled irrigation pump
- OLED status display
- Wi-Fi + MQTT cloud telemetry
- FreeRTOS multitasking
- Deep sleep battery optimization
- OTA firmware updates
- AI-assisted irrigation recommendation
- PCB and BOM planning
- 3D-printed enclosure plan
- Testing and deployment documentation

## System flow

```text
Sensors -> ESP32 -> FreeRTOS tasks -> MQTT cloud
                    |-> OLED
                    |-> Irrigation relay -> DC pump
                    |-> OTA
                    |-> Deep sleep
                    |-> AI recommendation
```

See `firmware/`, `ai/`, `mqtt/`, `hardware/`, `enclosure/`, `docs/`, and `tests/` for the implementation and engineering documentation.

> The AI module is advisory: keep a deterministic moisture threshold and maximum pump runtime as safety fallbacks.
