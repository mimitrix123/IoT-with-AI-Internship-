import tempfile
from database import EventStore

def test_event_round_trip():
    with tempfile.NamedTemporaryFile(suffix='.db') as f:
        store = EventStore(f.name)
        event_id = store.add_event('unknown', 0.91, 'data/test.jpg')
        row = store.recent(1)[0]
        assert row[0] == event_id
        assert row[2] == 'unknown'
        assert row[3] == 0.91
        store.close()
