"""Minimal Raspberry Pi smart-doorbell reference implementation."""
from datetime import datetime
from pathlib import Path
import cv2

CAPTURE_DIR = Path("captures")
CAPTURE_DIR.mkdir(exist_ok=True)


def capture_frame(camera_index=0):
    camera = cv2.VideoCapture(camera_index)
    if not camera.isOpened():
        raise RuntimeError("Camera could not be opened")
    ok, frame = camera.read()
    camera.release()
    if not ok:
        raise RuntimeError("Camera frame could not be captured")
    path = CAPTURE_DIR / f"visitor_{datetime.now():%Y%m%d_%H%M%S}.jpg"
    cv2.imwrite(str(path), frame)
    return path


def detect_person(image_path):
    image = cv2.imread(str(image_path))
    if image is None:
        return False
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Simple motion/brightness gate for a demo; replace with a trained detector
    # (e.g. MobileNet/YOLO) for production-quality person detection.
    return float(gray.mean()) > 15


def notify(image_path):
    print(f"Visitor event: {image_path}")
    # Integrate an authenticated notification service here.


if __name__ == "__main__":
    image = capture_frame()
    if detect_person(image):
        notify(image)
