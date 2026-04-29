from azure.storage.filedatalake import DataLakeServiceClient
from datetime import datetime
import json
import uuid
import os

DATALAKE_CONNECTION = os.getenv("DATALAKE_CONNECTION")


def get_partitioned_path(subfolder, file_name=None):
    now = datetime.utcnow()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    if file_name:
        return f"{subfolder}/year={year}/month={month}/day={day}/{file_name}.json"

    return f"{subfolder}/year={year}/month={month}/day={day}/{uuid.uuid4()}.json"


def get_file_client(file_system_name, subfolder, file_name=None):
    service_client = DataLakeServiceClient.from_connection_string(DATALAKE_CONNECTION)
    file_system_client = service_client.get_file_system_client(file_system_name)

    path = get_partitioned_path(subfolder, file_name=file_name)
    file_client = file_system_client.get_file_client(path)
    return file_client


def write_event(event_dict, file_system_name, subfolder, file_name=None):
    file_client = get_file_client(file_system_name, subfolder, file_name=file_name)

    data = json.dumps(event_dict, indent=2)
    data_bytes = data.encode("utf-8")

    file_client.create_file()
    file_client.append_data(data=data_bytes, offset=0, length=len(data_bytes))
    file_client.flush_data(len(data_bytes))