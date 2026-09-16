# PCB design plan

## Blocks
1. ESP32 module and programming header
2. 3.3 V regulated logic rail
3. Sensor connectors for soil, temperature and light
4. I2C OLED header
5. Pump driver/relay connector
6. Separate pump power input and fuse
7. Status LED and test points

## Layout guidance
- Keep pump current traces away from analog sensor traces.
- Place decoupling capacitors close to the ESP32/regulator.
- Use screw terminals for field wiring.
- Provide mounting holes and polarity labels.
- Use a transistor/MOSFET or properly isolated relay driver rather than driving a pump directly from GPIO.
