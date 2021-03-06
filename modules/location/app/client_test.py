
import os

import grpc
from google.protobuf.json_format import MessageToDict, MessageToJson

# from protobuf import person_pb2, person_pb2_grp
from protobuf import (connection_pb2, connection_pb2_grpc, person_pb2,
                      person_pb2_grpc)

#channel = grpc.insecure_channel("localhost:50051")
api_person_host = os.getenv("API_PERSON_HOST", "localhost")
api_location_host = os.getenv("API_LOCATION_HOST", "localhost")

api_person_host = "192.168.50.4"
api_location_host = "192.168.50.4"
from google.protobuf.json_format import MessageToDict, MessageToJson

# port 30002 has been mapped in the to from guest to host in the VM with vagrant
# Host: 192.168.50.4 or localhost
# Docker
# channel = grpc.insecure_channel("localhost:50051")

# For kubernetes
channel = grpc.insecure_channel(f"{api_person_host}:30003", options=(('grpc.enable_http_proxy', 0),))
# stub = person_pb2_grpc.PersonServiceStub(channel)
# location_stub = location_pb2_grpc.LocationServiceStub(channel)
connection_stub = connection_pb2_grpc.ConnectionServiceStub(channel)


connection_request = connection_pb2.GetConnectionRequest(
    person_id = 1,
    start_date = "2020-01-01", 
    end_date = "2020-12-30",
    meters = 6.0,
)
response3 = connection_stub.GetConnection(connection_request)

print("resppppp3\n", response3)
print("FORMATTEd", [MessageToDict(m, preserving_proto_field_name=True) for m in response3.connections])

# # person = person_pb2.CreatePersonRequest(
# #     first_name = "Kivi",
# #     last_name = "sto",
# #     company_name = "Wrong",
# # )


# # response = stub.CreatePerson(person) 
# # print("resppp", response)



# # response2 = stub.GetAllPersons(person_pb2.Empty())

# api_person_host = os.getenv("API_PERSON_HOST", "localhost")

# # port 30002 has been mapped in the to from guest to host in the VM with vagrant
# # Host: 192.168.50.4 or localhost
# channel = grpc.insecure_channel(f"{api_person_host}:50052")
# #channel = grpc.insecure_channel(f"{api_person_host}:30002", options=(('grpc.enable_http_proxy', 0),))
# stub = person_pb2_grpc.PersonServiceStub(channel)


# response3 = stub.GetPerson(person_pb2.GetPersonRequest(id=1))

# print("resppp3ll\n", response3)

# response = stub.GetAllPersons(person_pb2.Empty())
# print("resppp2KK", response)
# print("resppp2", [MessageToDict(m, preserving_proto_field_name=True) for m in response.persons])
