# Voice Control

The voice layer is designed as a local command adapter. Speech recognition can map phrases to a small allow-list of commands such as:

- `turn living room lights on`
- `turn bedroom lights off`
- `set thermostat to 22`
- `show home status`
- `enable away mode`

Recommended flow:

```text
Microphone -> speech-to-text -> intent parser -> allow-list validation -> MQTT command -> edge gateway -> device
```

For security, never execute arbitrary shell commands from speech. Require authentication for sensitive actions and keep the command vocabulary explicit.
