from flask import Flask, render_template_string
from database import EventStore

app = Flask(__name__)
store = EventStore("data/events.db")
TEMPLATE = '''<!doctype html><html><head><meta charset="utf-8"><title>AI Smart Doorbell</title><style>body{font-family:Arial;max-width:1100px;margin:40px auto;padding:0 20px}table{width:100%;border-collapse:collapse}th,td{padding:10px;border-bottom:1px solid #ddd;text-align:left}</style></head><body><h1>🚪 AI Smart Doorbell</h1><table><tr><th>Time</th><th>Visitor</th><th>Confidence</th><th>Snapshot</th><th>Notified</th></tr>{% for e in events %}<tr><td>{{e[1]}}</td><td>{{e[2]}}</td><td>{{'%.2f'|format(e[3])}}</td><td>{{e[4] or '-'}}</td><td>{{'Yes' if e[5] else 'No'}}</td></tr>{% endfor %}</table></body></html>'''

@app.get("/")
def index():
    return render_template_string(TEMPLATE, events=store.recent())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
