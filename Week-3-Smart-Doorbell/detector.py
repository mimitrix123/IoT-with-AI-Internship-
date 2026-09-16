from pathlib import Path
import cv2

class VisitorDetector:
    """OpenCV face detection with a replaceable TinyML classifier hook."""
    def __init__(self, config):
        self.face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        model = config.get("model", {})
        self.known_threshold = float(model.get("known_threshold", 0.70))
        self.known_dir = Path(model.get("known_faces_dir", "data/known"))
    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face.detectMultiScale(gray, 1.2, 5, minSize=(60, 60))
        if len(faces) == 0: return None
        x, y, w, h = max(faces, key=lambda b: b[2] * b[3])
        label, confidence = self.classify_face(frame[y:y+h, x:x+w])
        return {"label": label, "confidence": confidence, "box": (int(x), int(y), int(w), int(h))}
    def classify_face(self, crop):
        # Baseline: safely report unknown until a trained TinyML/TFLite model is supplied.
        return "unknown", 0.99
