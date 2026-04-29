import json
import os
from azure.storage.filedatalake import DataLakeServiceClient
from datetime import datetime

DATALAKE_CONNECTION = os.getenv("DATALAKE_CONNECTION")
FILE_SYSTEM_NAME = "silver"


def get_current_order_path(order_id):
    now = datetime.utcnow()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    return f"current_orders/year={year}/month={month}/day={day}/{order_id}.json"


def get_file_client(order_id):
    service_client = DataLakeServiceClient.from_connection_string(DATALAKE_CONNECTION)
    file_system_client = service_client.get_file_system_client(FILE_SYSTEM_NAME)
    path = get_current_order_path(order_id)
    return file_system_client.get_file_client(path)


def read_existing_current_order(order_id):
    file_client = get_file_client(order_id)

    try:
        download = file_client.download_file()
        content = download.readall().decode("utf-8")
        return json.loads(content)
    except Exception:
        return None


def should_overwrite_current_order(existing_record, incoming_record):
    if existing_record is None:
        return True

    existing_rank = existing_record.get("last_event_sequence_rank", 0)
    incoming_rank = incoming_record.get("last_event_sequence_rank", 0)

    if incoming_rank > existing_rank:
        return True

    if incoming_rank < existing_rank:
        return False

    existing_ts = existing_record.get("last_event_timestamp")
    incoming_ts = incoming_record.get("last_event_timestamp")

    if incoming_ts and existing_ts:
        return incoming_ts >= existing_ts

    return True