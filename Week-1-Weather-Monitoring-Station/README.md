# Week 1 — ESP32 Weather Monitoring Station

## Objective
Measure temperature and humidity with an ESP32 + DHT11 and publish telemetry to ThingSpeak.

## Hardware
- ESP32 development board
- DHT11 sensor
- Jumper wires and USB power

DHT11 data is connected to GPIO 4.

## Software
Arduino IDE, ESP32 board package, DHT sensor library, ThingSpeak library.

## Features
- Periodic temperature/humidity sampling
- ThingSpeak cloud upload
- Configurable upload interval
- Example secrets file with placeholders
- Threshold logic ready for alerts

## Setup
1. Copy `src/secrets.example.h` to `src/secrets.h`.
2. Fill in Wi-Fi and ThingSpeak credentials.
3. Install required Arduino libraries.
4. Flash `src/weather_station.ino`.
5. Open Serial Monitor and verify telemetry.

Never commit real credentials.
