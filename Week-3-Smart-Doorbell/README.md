# Week 3 — AI Smart Doorbell

Raspberry Pi camera doorbell that captures a visitor image, runs lightweight computer vision, and triggers a notification workflow.

## Architecture
Camera → Raspberry Pi → OpenCV/person detection → event log → notification adapter.

## Features
- Camera capture on doorbell event
- Person/visitor detection hook
- Timestamped event records
- Configurable notification adapter
- Local-first processing so images need not leave the device

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python smart_doorbell.py
```

On Raspberry Pi OS, install the camera stack appropriate for your camera module. The notification function is deliberately a local adapter placeholder so secrets are not stored in source code.
