
import grpc
import os
from protobuf import person_pb2, person_pb2_grpc
from google.protobuf.json_format import MessageToJson, MessageToDict
#channel = grpc.insecure_channel("localhost:50051")
api_person_host = os.getenv("API_PERSON_HOST", "localhost")

# port 30002 has been mapped in the to from guest to host in the VM with vagrant
# Host: 192.168.50.4 or localhost
channel = grpc.insecure_channel(f"{api_person_host}:50052", options=(('grpc.enable_http_proxy', 0),))
#channel = grpc.insecure_channel(f"{api_person_host}:30002", options=(('grpc.enable_http_proxy', 0),))
stub = person_pb2_grpc.PersonServiceStub(channel)


# person = person_pb2.CreatePersonRequest(
#     first_name = "Kivi",
#     last_name = "sto",
#     company_name = "Wrong",
# )


# response = stub.CreatePerson(person) 
# print("resppp", response)


response3 = stub.GetPerson(person_pb2.GetPersonRequest(id=1))

print("resppp3ll\n", response3)

response = stub.GetAllPersons(person_pb2.Empty())
print("resppp2KK", response)
print("resppp2", [MessageToDict(m, preserving_proto_field_name=True) for m in response.persons])
