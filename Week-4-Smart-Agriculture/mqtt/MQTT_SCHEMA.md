# MQTT schema

Topic: `farm/{plot_id}/telemetry`

Example payload:

```json
{"soil_raw":1450,"temperature_raw":2100,"light_raw":730,"pump":true}
```

Recommended command topic: `farm/{plot_id}/command`

Commands should be authenticated and validated before controlling the pump. Do not expose an unauthenticated MQTT broker to the public internet.
