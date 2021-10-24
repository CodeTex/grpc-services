from pathlib import Path
import json
from typing import List

import station_data_pb2
import station_data_pb2_grpc


class StationDataServer(station_data_pb2_grpc.StationDataServiceServicer):
    data_dir = Path(__file__).resolve().parent[3] / "data"

    def __init__(self) -> None:
        self.db = self.read_json_file(self.data_dir)

    def GetLatest(self, request, context):
        return super().GetLatest(request, context)

    def GetRecords(self, request, context):
        return super().GetRecords(request, context)

    @staticmethod
    def read_json_file(data_dir: Path) -> List:
        data_list: List = []
        with open(data_dir / "meas_data.json") as f:
            for item in json.load(f):
                record = station_data_pb2.Record(
                    _id=item["_id"],
                    name=item["name"],
                    value=item["value"],
                    time=item["time"],
                )
                data_list.append(record)
        return data_list
