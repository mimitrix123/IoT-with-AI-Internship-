from datetime import datetime
import sqlite3

class EventStore:
    def __init__(self, path):
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL, label TEXT NOT NULL, confidence REAL NOT NULL, snapshot TEXT, notified INTEGER NOT NULL DEFAULT 0)")
        self.db.commit()
    def add_event(self, label, confidence, snapshot, notified=False):
        cur = self.db.execute("INSERT INTO events(timestamp,label,confidence,snapshot,notified) VALUES(?,?,?,?,?)", (datetime.now().isoformat(timespec="seconds"), label, float(confidence), snapshot, int(notified)))
        self.db.commit()
        return cur.lastrowid
    def mark_notified(self, event_id, notified):
        self.db.execute("UPDATE events SET notified=? WHERE id=?", (int(notified), event_id)); self.db.commit()
    def recent(self, limit=50):
        return self.db.execute("SELECT id,timestamp,label,confidence,snapshot,notified FROM events ORDER BY id DESC LIMIT ?", (int(limit),)).fetchall()
    def close(self): self.db.close()
