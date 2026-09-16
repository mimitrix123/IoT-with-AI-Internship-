# IoT with AI Internship

A four-week IoT + AI engineering portfolio. Week 4 is a complete AI-powered smart home platform using ESP32/Raspberry Pi, multi-sensor monitoring, occupancy prediction, energy optimization, real-time dashboarding, voice control, mobile notifications, encrypted communication, and deployment documentation.

## Projects

| Week | Project | Main technologies |
|---|---|---|
| 1 | Weather Monitoring Station | ESP32, DHT11, ThingSpeak |
| 2 | Predictive Maintenance | Python, pandas, scikit-learn, MQTT |
| 3 | AI Smart Doorbell | Raspberry Pi, camera, OpenCV, Python |
| 4 | AI Smart Home | ESP32/Raspberry Pi, sensors, MQTT/TLS, FreeRTOS, Python ML, dashboard, voice, notifications |

## Week 4 — AI-Powered Smart Home System

### Features
- Temperature, motion, light and sound sensing
- ESP32 sensor nodes with Raspberry Pi edge gateway option
- AI occupancy prediction from sensor history
- AI energy optimization recommendations
- Real-time MQTT dashboard with room/device status
- Voice-control integration through a local command interface
- Mobile notification workflow for important events
- Encrypted MQTT/TLS communication and credential separation
- FreeRTOS multitasking on ESP32
- OTA firmware update strategy
- Deployment, testing, architecture and security documentation

## Architecture

```text
 Temperature ─┐
 Motion ──────┤
 Light ───────┼──> ESP32 Sensor Node ──MQTT/TLS──> Raspberry Pi Edge Gateway
 Sound ───────┘                                      │
                                                     ├──> AI Occupancy Model
                                                     ├──> AI Energy Optimizer
                                                     ├──> Real-time Dashboard
                                                     ├──> Voice Control
                                                     └──> Mobile Notifications

                    FreeRTOS tasks on ESP32
                    Sensors | MQTT | Health | OTA
```

## Repository structure

```text
Week-1-Weather-Monitoring-Station/
Week-2-Predictive-Maintenance/
Week-3-Smart-Doorbell/
Week-4-Smart-Home/
├── firmware/esp32-smart-home/
├── edge/raspberry-pi/
├── ai/
├── dashboard/
├── voice/
├── notifications/
├── security/
├── hardware/
├── docs/
└── tests/
```

Secrets such as Wi-Fi passwords, MQTT credentials, API keys, certificates and notification tokens must never be committed. Use local environment variables/configuration excluded by `.gitignore`.

## Safety and security
Use low-voltage prototype electronics and appropriately rated power supplies. Keep device credentials private, validate commands at the edge, use TLS for network traffic, and fail to a safe device state when connectivity or AI inference is unavailable.
