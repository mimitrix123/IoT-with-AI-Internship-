# Week 4 — AI-Powered Smart Home

A complete reference architecture for an AI-enabled home automation platform.

## Goals

Build a system that senses room conditions, predicts occupancy, recommends energy-saving actions, exposes a real-time dashboard, accepts voice commands, sends mobile notifications, and protects communication with TLS.

## Hardware
- ESP32 sensor node(s)
- Raspberry Pi edge gateway
- Temperature sensor
- PIR/mmWave motion sensor
- LDR or digital ambient-light sensor
- Sound-level sensor
- Optional relay/LED/fan/load actuator
- OLED status display (optional)

## Data flow

```text
Sensors -> ESP32/FreeRTOS -> MQTT/TLS -> Raspberry Pi
                                      -> time-series storage
                                      -> occupancy AI
                                      -> energy AI
                                      -> dashboard
                                      -> voice command service
                                      -> notification service
```

## AI layer
1. **Occupancy prediction:** classify occupied/unoccupied from recent temperature, motion, light and sound features.
2. **Energy optimization:** estimate an energy-saving action from occupancy, temperature, light and device state.
3. **Safety fallback:** AI never directly overrides safety-critical controls. If inference is unavailable, use deterministic rules and safe defaults.

## Deliverables
- `firmware/` — ESP32 sensor-node reference firmware
- `edge/` — Raspberry Pi MQTT gateway/service
- `ai/` — training, inference and sample data
- `dashboard/` — real-time dashboard starter
- `voice/` — local voice-command interface
- `notifications/` — mobile alert adapter
- `security/` — TLS, secrets and threat-model guidance
- `hardware/` — BOM and pinout
- `docs/` — architecture and deployment
- `tests/` — validation plan

## Deployment
Run the Raspberry Pi services on the LAN, use an authenticated MQTT broker with TLS, store secrets outside Git, and expose only the minimum required ports. Use OTA only through an authenticated maintenance path.
