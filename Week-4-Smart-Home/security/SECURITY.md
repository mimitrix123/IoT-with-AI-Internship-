# Security Design

## Transport
- Use MQTT over TLS (normally port 8883).
- Validate the broker certificate and avoid insecure plaintext MQTT in production.
- Use unique credentials/certificates per device where practical.

## Secrets
- Keep Wi-Fi passwords, MQTT credentials, API tokens and private keys outside Git.
- Prefer environment variables or a Raspberry Pi secret manager.
- Rotate credentials if a device is lost or compromised.

## Command security
- Subscribe devices only to the topics they need.
- Validate command schema, ranges and device ownership at the edge.
- Use an explicit allow-list for voice intents.
- Log security-relevant events without storing unnecessary personal data.

## AI security
AI recommendations are untrusted inputs. Apply deterministic bounds, user-configured constraints and safe fallbacks before actuator commands are executed.
