# Test plan

- [ ] Sensor ADC readings remain stable over repeated samples.
- [ ] Soil calibration maps dry/wet conditions correctly.
- [ ] OLED updates without blocking sensor acquisition.
- [ ] MQTT reconnects after Wi-Fi loss.
- [ ] Telemetry payload validates against the documented schema.
- [ ] Pump remains OFF after boot/reset.
- [ ] Pump runtime never exceeds configured maximum.
- [ ] OTA update succeeds from a trusted local network.
- [ ] Deep sleep wakes on schedule and reconnects to Wi-Fi/MQTT.
- [ ] AI model training completes on sample data.
- [ ] AI recommendation does not bypass deterministic pump safety limits.
