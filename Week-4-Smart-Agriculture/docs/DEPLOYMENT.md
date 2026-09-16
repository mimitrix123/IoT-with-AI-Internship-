# Deployment checklist

1. Copy `config.example.h` to a private local `config.h` and fill credentials.
2. Calibrate the soil sensor in dry and well-watered soil.
3. Verify the relay output with the pump disconnected.
4. Verify pump current, supply voltage, fuse and driver rating.
5. Connect the pump and perform a short controlled run.
6. Configure MQTT authentication/TLS when supported by the broker.
7. Upload firmware over USB first; enable OTA after the first stable boot.
8. Test Wi-Fi/MQTT reconnection and power-cycle recovery.
9. Validate deep sleep current and wake-up behavior on the actual battery.
10. Record calibration values and field-test results.
