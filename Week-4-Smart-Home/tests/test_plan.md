# Test Plan

## Functional
- Verify all four sensor streams and calibration.
- Verify MQTT/TLS connection and reconnect behavior.
- Verify dashboard updates and stale-data indicators.
- Verify voice allow-list and command validation.
- Verify mobile notification delivery and duplicate suppression.

## AI
- Hold out test data and report precision, recall and confusion matrix.
- Test missing/noisy sensor values.
- Compare AI recommendations with deterministic fallback rules.
- Reject recommendations outside configured comfort/safety limits.

## Reliability/security
- Power-cycle ESP32 and Raspberry Pi.
- Disconnect Wi-Fi and broker, then restore connectivity.
- Test OTA authentication and rollback/recovery procedure.
- Confirm no secrets are committed.
- Confirm MQTT topics enforce least privilege.
