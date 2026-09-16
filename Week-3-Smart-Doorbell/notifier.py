import base64
from pathlib import Path
import requests

class WebhookNotifier:
    def __init__(self, config):
        self.url = config.get("webhook_url", "")
        self.timeout = float(config.get("timeout_seconds", 5))
    def send(self, label, confidence, snapshot: Path):
        if not self.url: return False
        payload = {"event":"smart_doorbell", "visitor":label, "confidence":round(float(confidence),4), "snapshot_name":snapshot.name, "snapshot_base64":base64.b64encode(snapshot.read_bytes()).decode("ascii")}
        try:
            return requests.post(self.url, json=payload, timeout=self.timeout).ok
        except requests.RequestException:
            return False
