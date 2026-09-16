# Week 4 — AI Smart Home

An end-to-end reference architecture combining ESP32/Raspberry Pi sensors, MQTT, AI-based occupancy/energy inference, automation, dashboard telemetry, voice-control integration points, and encrypted communication.

## Architecture

```text
Sensors/Actuators → ESP32 → MQTT broker → Smart-home service → Dashboard
                                      ↘ AI occupancy/energy model
                                      ↘ Notification/voice adapters
```

## Sensor inputs
Temperature, motion, light, and sound level. Actuators can control low-voltage lights, fans, or other safe loads through appropriate driver hardware.

## AI goals
- Estimate occupancy from sensor features.
- Predict near-term energy demand.
- Recommend or trigger energy-saving actions under configurable rules.

## Security
Use TLS-enabled MQTT, unique device credentials, least-privilege topics, network segmentation, and never commit certificates or passwords.

## Run the demo
```bash
pip install -r requirements.txt
python smart_home.py
```
