import time
from pathlib import Path
import cv2
import yaml
from database import EventStore
from detector import VisitorDetector
from notifier import WebhookNotifier

def main():
    config = yaml.safe_load(Path("config.yaml").read_text())
    store = EventStore(config["database"]["path"])
    detector = VisitorDetector(config)
    notifier = WebhookNotifier(config.get("notification", {}))
    camera = cv2.VideoCapture(config.get("camera", {}).get("device", 0))
    if not camera.isOpened():
        raise RuntimeError("Unable to open camera")
    cooldown = float(config.get("camera", {}).get("cooldown_seconds", 10))
    last_event = 0.0
    output_dir = Path(config.get("camera", {}).get("snapshot_dir", "data/snapshots"))
    output_dir.mkdir(parents=True, exist_ok=True)
    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                continue
            result = detector.detect(frame)
            now = time.time()
            if result and now - last_event >= cooldown:
                last_event = now
                filename = output_dir / f"visitor_{int(now)}.jpg"
                cv2.imwrite(str(filename), frame)
                event_id = store.add_event(result["label"], result["confidence"], str(filename))
                store.mark_notified(event_id, notifier.send(result["label"], result["confidence"], filename))
            if config.get("camera", {}).get("display", False):
                cv2.imshow("Smart Doorbell", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        camera.release()
        cv2.destroyAllWindows()
        store.close()

if __name__ == "__main__":
    main()
