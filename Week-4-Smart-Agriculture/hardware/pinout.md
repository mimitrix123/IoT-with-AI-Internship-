# ESP32 pinout

| Function | GPIO | Interface |
|---|---:|---|
| Soil moisture | 34 | ADC |
| Temperature sensor input | 35 | ADC placeholder; adapt to digital sensor if used |
| Light sensor | 32 | ADC |
| Pump relay | 26 | Digital output |
| OLED SDA | 21 | I2C |
| OLED SCL | 22 | I2C |

Avoid ADC pins connected to noisy high-current pump wiring. Keep sensor ground/reference routing clean.
