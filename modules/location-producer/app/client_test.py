
import os

import grpc
from google.protobuf.json_format import MessageToDict, MessageToJson

# from protobuf import person_pb2, person_pb2_grp
from protobuf import (location_pb2, location_pb2_grpc)

api_location_producer_host = os.getenv("API_LOCATION_PRODUCER_HOST", "localhost")

api_person_host = "192.168.50.4"
api_location_host = "192.168.50.4"
from google.protobuf.json_format import MessageToDict, MessageToJson

# port 30002 has been mapped in the to from guest to host in the VM with vagrant

# For kubernetes
channel = grpc.insecure_channel(f"{api_person_host}:30004", options=(('grpc.enable_http_proxy', 0),))
location_stub = location_pb2_grpc.LocationServiceStub(channel)


location_request = location_pb2.CreateLocationRequest(
    person_id = 1,
    longitude = "64",
    latitude = "22",
)
response = location_stub.CreateLocation(location_request)

print("resppppp3\n", response)
print("FORMATTEd", MessageToDict(response, preserving_proto_field_name=True))
