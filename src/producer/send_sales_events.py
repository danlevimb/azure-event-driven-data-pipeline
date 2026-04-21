import json
import time
from datetime import datetime
import uuid

def build_event():
    return {
        "event_id": f"evt-{uuid.uuid4()}",
        "event_type": "order_created",
        "schema_version": "1.0",
        "source_system": "local-simulator",
        "event_time": datetime.utcnow().isoformat() + "Z",
        "payload": {
            "order_id": f"ORD-{uuid.uuid4().hex[:6].upper()}",
            "customer_id": f"CUST-{uuid.uuid4().hex[:4].upper()}",
            "order_total": round(100 + (1000 * uuid.uuid4().int % 10), 2),
            "currency": "MXN",
            "status": "CREATED"
        }
    }

def send_events(n=5, delay=1):
    for i in range(n):
        event = build_event()
        print(json.dumps(event, indent=2))
        print("-" * 50)
        time.sleep(delay)

if __name__ == "__main__":
    send_events(n=5, delay=1)
