# IoT with AI Internship

A four-week IoT + AI engineering portfolio. Week 4 is a complete ESP32 smart agriculture platform with sensing, automated irrigation, MQTT cloud telemetry, FreeRTOS multitasking, deep-sleep power management, OTA firmware updates, PCB planning, and a 3D-printable enclosure plan.

## Projects

| Week | Project | Main technologies |
|---|---|---|
| 1 | Weather Monitoring Station | ESP32, DHT11, ThingSpeak |
| 2 | Predictive Maintenance | Python, pandas, scikit-learn, MQTT |
| 3 | AI Smart Doorbell | Raspberry Pi, camera, OpenCV, Python |
| 4 | Smart Agriculture + AI | ESP32, FreeRTOS, MQTT, OLED, relay, OTA, deep sleep, Python ML |

## Week 4 — IoT Smart Agriculture System

### Features
- ESP32 soil-moisture, temperature and light monitoring
- Automatic irrigation using a relay-controlled DC water pump
- OLED local status display
- Wi-Fi connectivity and MQTT cloud reporting
- FreeRTOS tasks for sensing, display, MQTT and irrigation control
- Deep sleep strategy for battery-powered operation
- OTA firmware update support
- AI-assisted irrigation recommendation using sensor history
- PCB design, BOM and wiring documentation
- 3D-printed enclosure plan
- Testing, deployment and troubleshooting documentation

## Architecture

```text
 Soil Moisture ─┐
 Temperature ───┼──> ESP32 ──> MQTT Broker / Cloud
 Light Sensor ──┘      │
                       ├──> OLED Display
                       ├──> Relay ──> Water Pump
                       ├──> OTA Firmware
                       └──> AI Irrigation Recommendation

          FreeRTOS task scheduler
                       │
                  Deep Sleep
```

## Repository structure

```text
Week-1-Weather-Monitoring-Station/
Week-2-Predictive-Maintenance/
Week-3-Smart-Doorbell/
Week-4-Smart-Agriculture/
├── firmware/esp32-smart-agriculture/
├── ai/
├── mqtt/
├── hardware/
├── enclosure/
├── docs/
└── tests/
```

Secrets such as Wi-Fi passwords, MQTT credentials, API keys and OTA passwords must never be committed. Use environment variables or a local `config.h` excluded by `.gitignore`.

## Safety
Use isolated low-voltage electronics and an appropriately rated DC pump/relay. Never connect prototype ESP32 GPIO pins directly to mains voltage. Use suitable fusing, flyback protection and power isolation for the pump circuit.
