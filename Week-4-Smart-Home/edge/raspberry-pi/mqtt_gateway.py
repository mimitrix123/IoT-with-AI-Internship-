"""Minimal Raspberry Pi MQTT edge gateway.

For production, configure TLS certificates, authentication, persistent storage,
message validation and a supervised service (systemd/Docker).
"""
import json
import os
import paho.mqtt.client as mqtt

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "8883"))
TOPIC = os.getenv("MQTT_TOPIC", "home/+/telemetry")


def on_connect(client, userdata, flags, reason_code, properties=None):
    print("MQTT connected:", reason_code)
    client.subscribe(TOPIC, qos=1)


def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        print(message.topic, data)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        print("Rejected malformed payload:", exc)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="smart-home-gateway")
client.on_connect = on_connect
client.on_message = on_message
client.tls_set()  # Uses system CA store; configure client certs if required.

if __name__ == "__main__":
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_forever()
