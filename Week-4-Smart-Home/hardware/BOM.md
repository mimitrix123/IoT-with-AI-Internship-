# Hardware BOM

| Component | Purpose |
|---|---|
| ESP32 DevKit | Sensor/edge node |
| DHT22 or DS18B20 | Temperature |
| PIR or mmWave sensor | Motion/presence |
| LDR or BH1750 | Ambient light |
| Analog sound sensor | Sound level |
| OLED I2C display | Local status |
| Raspberry Pi | Gateway + AI + dashboard |
| Optional relay/MOSFET module | Low-voltage actuator control |
| Appropriate power supply | Stable device power |

Use a properly rated driver, flyback protection and fuse for inductive loads. Do not connect mains loads directly to ESP32 GPIO pins.
