```text
PS C:\azure-event-driven-data-pipeline> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\azure-event-driven-data-pipeline\.venv\Scripts\Activate.ps1)
(.venv) PS C:\azure-event-driven-data-pipeline> & c:\azure-event-driven-data-pipeline\.venv\Scripts\python.exe c:/azure-event-driven-data-pipeline/producer/send_sales_events.py
c:\azure-event-driven-data-pipeline\producer\send_sales_events.py:65: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  "event_time": datetime.utcnow().isoformat() + "Z",
SCENARIO=paid_order
{
  "event_id": "evt-139b2e49-5cbb-4ce0-8cc1-a4ed0fb22b21",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:19:59.429072Z",
  "payload": {
    "order_id": "ORD-A8412C",
    "customer_id": "CUST-FEEB",
    "order_total": 450.75,
    "currency": "USD",
    "status": "CREATED"
  }
}
------------------------------------------------------------
SCENARIO=paid_order
{
  "event_id": "evt-d8da08a0-030a-417f-b743-82a89cf71b4f",
  "event_type": "payment_confirmed",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:04.987737Z",
  "payload": {
    "order_id": "ORD-A8412C",
    "customer_id": "CUST-FEEB",
    "order_total": 450.75,
    "currency": "USD",
    "status": "PAID"
  }
}
------------------------------------------------------------
SCENARIO=cancelled_order
{
  "event_id": "evt-487fadb4-01ef-44cb-b6be-091ea940626d",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:06.248712Z",
  "payload": {
    "order_id": "ORD-8CF749",
    "customer_id": "CUST-20D2",
    "order_total": 320.45,
    "currency": "USD",
    "status": "CREATED"
  }
}
------------------------------------------------------------
SCENARIO=cancelled_order
{
  "event_id": "evt-41901115-7660-48b8-a432-3f991bd19076",
  "event_type": "order_cancelled",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:07.313308Z",
  "payload": {
    "order_id": "ORD-8CF749",
    "customer_id": "CUST-20D2",
    "order_total": 320.45,
    "currency": "USD",
    "status": "CANCELLED"
  }
}
------------------------------------------------------------
SCENARIO=paid_then_cancelled
{
  "event_id": "evt-854c0dbd-a840-4000-992b-b1d4419ffb3f",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:08.378501Z",
  "payload": {
    "order_id": "ORD-0C0A5B",
    "customer_id": "CUST-B620",
    "order_total": 1250.0,
    "currency": "MXN",
    "status": "CREATED"
  }
}
------------------------------------------------------------
SCENARIO=paid_then_cancelled
{
  "event_id": "evt-3f8c4289-18ff-4237-91ff-6660c8ffac19",
  "event_type": "payment_confirmed",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:09.447241Z",
  "payload": {
    "order_id": "ORD-0C0A5B",
    "customer_id": "CUST-B620",
    "order_total": 1250.0,
    "currency": "MXN",
    "status": "PAID"
  }
}
------------------------------------------------------------
SCENARIO=paid_then_cancelled
{
  "event_id": "evt-9f4ec1fd-31bb-410a-9de2-601149146eca",
  "event_type": "order_cancelled",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:10.513304Z",
  "payload": {
    "order_id": "ORD-0C0A5B",
    "customer_id": "CUST-B620",
    "order_total": 1250.0,
    "currency": "MXN",
    "status": "CANCELLED"
  }
}
------------------------------------------------------------
SCENARIO=open_order
{
  "event_id": "evt-c9806f81-e63e-4d53-aab5-12dbd53c9600",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:11.637309Z",
  "payload": {
    "order_id": "ORD-539E70",
    "customer_id": "CUST-6136",
    "order_total": 275.9,
    "currency": "MXN",
    "status": "CREATED"
  }
}
------------------------------------------------------------
SCENARIO=high_value_paid
{
  "event_id": "evt-91ac2886-9656-4d43-bf6a-d31fef1adcd1",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:12.719076Z",
  "payload": {
    "order_id": "ORD-9552A9",
    "customer_id": "CUST-035F",
    "order_total": 4200.0,
    "currency": "USD",
    "status": "CREATED"
  }
}
------------------------------------------------------------
SCENARIO=high_value_paid
{
  "event_id": "evt-4910d208-4033-4e9d-a2c0-23a428ce09fd",
  "event_type": "payment_confirmed",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:13.785251Z",
  "payload": {
    "order_id": "ORD-9552A9",
    "customer_id": "CUST-035F",
    "order_total": 4200.0,
    "currency": "USD",
    "status": "PAID"
  }
}
------------------------------------------------------------
SCENARIO=zero_amount
{
  "event_id": "evt-981468d0-94d2-4b2a-893a-69b010e8615b",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:14.851101Z",
  "payload": {
    "order_id": "ORD-28C101",
    "customer_id": "CUST-E4F1",
    "order_total": 0.0,
    "currency": "USD",
    "status": "CREATED"
  }
}
------------------------------------------------------------
SCENARIO=bad_currency
{
  "event_id": "evt-da694325-5e16-49b9-818f-d1ec510ee94b",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:15.922236Z",
  "payload": {
    "order_id": "ORD-92BAC2",
    "customer_id": "CUST-0BD7",
    "order_total": 150.0,
    "currency": "EUR",
    "status": "CREATED"
  }
}
------------------------------------------------------------
SCENARIO=bad_status
{
  "event_id": "evt-dd095084-2d98-447b-996f-c97389797c2e",
  "event_type": "order_created",
  "schema_version": "1.0",
  "source_system": "local-simulator",
  "event_time": "2026-04-30T21:20:16.996814Z",
  "payload": {
    "order_id": "ORD-0FE12F",
    "customer_id": "CUST-008A",
    "order_total": 200.0,
    "currency": "USD",
    "status": "PENDING_X"
  }
}
------------------------------------------------------------
✔ portfolio demo batch enviado | scenarios=8 | events_sent=13
(.venv) PS C:\azure-event-driven-data-pipeline> 
```