# 🚪 Week 3 — AI Smart Doorbell

A Raspberry Pi smart doorbell that captures visitors, detects faces, classifies visitors as **known** or **unknown** using a lightweight/TinyML-compatible model, sends notifications with snapshots, and records events for a dashboard.

## Features

- Raspberry Pi camera capture
- Face detection with OpenCV
- Lightweight visitor classification pipeline
- Known vs unknown visitor decision
- Snapshot capture for detected visitors
- Notification integration through a configurable webhook
- SQLite event logging
- Flask dashboard for visitor history
- Configurable confidence threshold and cooldown
- Privacy-friendly local processing by default

## Architecture

```text
Doorbell / Camera
       ↓
Raspberry Pi Camera
       ↓
Face Detection
       ↓
Lightweight Classifier
       ↓
Known / Unknown
   ↙          ↘
Snapshot    Snapshot
   ↓            ↓
Notification   Event Log
        \       /
         SQLite DB
             ↓
       Flask Dashboard
```

## Project Structure

```text
Week-3-Smart-Doorbell/
├── README.md
├── requirements.txt
├── config.example.yaml
├── app.py
├── detector.py
├── notifier.py
├── database.py
├── dashboard.py
├── model/
│   └── README.md
├── data/
│   └── .gitkeep
└── tests/
    └── test_database.py
```

## Hardware

- Raspberry Pi 4/5 recommended
- Raspberry Pi Camera Module or compatible USB camera
- Push button for the doorbell trigger
- Optional buzzer/LED
- Wi-Fi connection

## Software

- Python 3.10+
- OpenCV
- Flask
- SQLite
- NumPy
- PyYAML

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config.example.yaml config.yaml
```

On Raspberry Pi OS, enable the camera using the current Raspberry Pi camera configuration tools and verify the camera before starting the application.

## Run

```bash
python app.py
```

Open the dashboard at:

```text
http://<RASPBERRY_PI_IP>:5000
```

## TinyML model

The `model/` directory documents the expected model interface. A production deployment can use TensorFlow Lite/LiteRT or another embedded inference runtime. The application keeps model loading separate from camera and notification logic so the classifier can be replaced without redesigning the system.

Do **not** commit real face images, credentials, API tokens, or private visitor data.

## Notification configuration

Set a webhook URL in `config.yaml`. The notification payload includes the visitor classification and snapshot path/metadata. Replace the webhook implementation with Telegram, email, MQTT, Home Assistant, or another approved notification service as required.

## Dashboard

The Flask dashboard exposes recent events including:

- Timestamp
- Classification
- Confidence
- Snapshot filename
- Notification status

## Testing

```bash
pytest -q
```

## Security & privacy

- Keep visitor images on the local device unless notification delivery requires transmission.
- Use HTTPS for remote dashboard access.
- Protect the dashboard with authentication before exposing it outside the LAN.
- Store credentials outside source control.
- Add a retention policy for snapshots and event records.

## Learning outcomes

- Raspberry Pi camera programming
- Computer vision fundamentals
- Lightweight ML/TinyML deployment concepts
- Event-driven IoT design
- Notification APIs/webhooks
- SQLite data logging
- Flask dashboard development
- Security and privacy considerations for camera systems
