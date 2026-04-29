import json
import os
import random
import time
import uuid

from datetime import datetime
from pathlib import Path
from azure.eventhub import EventHubProducerClient, EventData

def load_local_settings():
    settings_path = Path(__file__).resolve().parents[1] / "local.settings.json"

    with open(settings_path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    for key, value in settings.get("Values", {}).items():
        os.environ.setdefault(key, value)
        
load_local_settings()

CONNECTION_STRING = os.getenv("PRODUCER_EVENT_HUB_CONNECTION")
EVENT_HUB_NAME = "sales-order"

def generate_currency(test_mode=None):
    if test_mode == "force_bad_currency":
        return "EUR"

    return random.choice(["MXN", "USD"])


def generate_status(test_mode=None, event_type="order_created"):
    if test_mode == "force_bad_status":
        return "PENDING_X"

    status_map = {
        "order_created": "CREATED",
        "payment_confirmed": "PAID",
        "order_cancelled": "CANCELLED"
    }

    return status_map.get(event_type, "CREATED")


def generate_order_total(test_mode=None):
    if test_mode == "force_zero":
        return 0.00

    rand = random.random()

    if rand < 0.10:
        return 0.00
    elif rand < 0.70:
        return round(random.uniform(50, 800), 2)
    else:
        return round(random.uniform(800, 5000), 2)


def build_event(test_mode=None, event_type="order_created", order_id=None, customer_id=None, order_total=None, currency=None):
    return {
        "event_id": f"evt-{uuid.uuid4()}",
        "event_type": event_type,
        "schema_version": "1.0",
        "source_system": "local-simulator",
        "event_time": datetime.utcnow().isoformat() + "Z",
        "payload": {
            "order_id": order_id or f"ORD-{uuid.uuid4().hex[:6].upper()}",
            "customer_id": customer_id or f"CUST-{uuid.uuid4().hex[:4].upper()}",
            "order_total": order_total if order_total is not None else generate_order_total(test_mode),
            "currency": currency or generate_currency(test_mode),
            "status": generate_status(test_mode, event_type)
        }
    }


def send_single_events(n=5, delay=0, test_mode=None):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        eventhub_name=EVENT_HUB_NAME
    )

    with producer:
        for _ in range(n):
            event = build_event(test_mode=test_mode)
            event_data = EventData(json.dumps(event))
            producer.send_batch([event_data])

            print(json.dumps(event, indent=2))
            print("-" * 60)

            if delay > 0:
                time.sleep(delay)

    print(f"✔ {n} eventos enviados a Event Hub | mode={test_mode or 'normal'}")


def send_same_order_lifecycle(delay=0):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        eventhub_name=EVENT_HUB_NAME
    )

    shared_order_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"
    shared_customer_id = f"CUST-{uuid.uuid4().hex[:4].upper()}"
    shared_order_total = round(random.uniform(100, 3000), 2)
    shared_currency = random.choice(["MXN", "USD"])

    lifecycle_events = [
        build_event(
            event_type="order_created",
            order_id=shared_order_id,
            customer_id=shared_customer_id,
            order_total=shared_order_total,
            currency=shared_currency
        ),
        build_event(
            event_type="payment_confirmed",
            order_id=shared_order_id,
            customer_id=shared_customer_id,
            order_total=shared_order_total,
            currency=shared_currency
        ),
        build_event(
            event_type="order_cancelled",
            order_id=shared_order_id,
            customer_id=shared_customer_id,
            order_total=shared_order_total,
            currency=shared_currency
        )
    ]

    with producer:
        for event in lifecycle_events:
            event_data = EventData(json.dumps(event))
            producer.send_batch([event_data])

            print(json.dumps(event, indent=2))
            print("-" * 60)

            if delay > 0:
                time.sleep(delay)

    print(f"✔ lifecycle enviado para {shared_order_id}")


def send_portfolio_demo_batch(delay=1):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STRING,
        eventhub_name=EVENT_HUB_NAME
    )

    scenarios = [
        ("paid_order", ["order_created", "payment_confirmed"], 450.75, "USD"),
        ("cancelled_order", ["order_created", "order_cancelled"], 320.45, "USD"),
        ("paid_then_cancelled", ["order_created", "payment_confirmed", "order_cancelled"], 1250.00, "MXN"),
        ("open_order", ["order_created"], 275.90, "MXN"),
        ("high_value_paid", ["order_created", "payment_confirmed"], 4200.00, "USD"),
        ("zero_amount", ["order_created"], 0.00, "USD"),
        ("bad_currency", ["order_created"], 150.00, "EUR"),
        ("bad_status", ["order_created"], 200.00, "USD"),
    ]

    events_sent = 0

    with producer:
        for scenario_name, event_types, order_total, currency in scenarios:
            shared_order_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"
            shared_customer_id = f"CUST-{uuid.uuid4().hex[:4].upper()}"

            for event_type in event_types:
                test_mode = None

                if scenario_name == "bad_currency":
                    test_mode = "force_bad_currency"

                if scenario_name == "bad_status":
                    test_mode = "force_bad_status"

                event = build_event(
                    test_mode=test_mode,
                    event_type=event_type,
                    order_id=shared_order_id,
                    customer_id=shared_customer_id,
                    order_total=order_total,
                    currency=currency
                )

                event_data = EventData(json.dumps(event))
                producer.send_batch([event_data])

                events_sent += 1

                print(f"SCENARIO={scenario_name}")
                print(json.dumps(event, indent=2))
                print("-" * 60)

                if delay > 0:
                    time.sleep(delay)

    print(f"✔ portfolio demo batch enviado | scenarios={len(scenarios)} | events_sent={events_sent}")

if __name__ == "__main__":
    TEST_MODE = "force_bad_status"
    # Opciones:
    # None
    # "force_zero"
    # "force_bad_currency"
    # "force_bad_status"
    # "same_order_lifecycle"
    # "portfolio_demo_batch"

    if not CONNECTION_STRING:
        raise ValueError("Missing PRODUCER_EVENT_HUB_CONNECTION environment variable.")

    if TEST_MODE == "portfolio_demo_batch":
        send_portfolio_demo_batch(delay=1)
    elif TEST_MODE == "same_order_lifecycle":
        send_same_order_lifecycle(delay=1)
    else:
        send_single_events(n=5, delay=0, test_mode=TEST_MODE)