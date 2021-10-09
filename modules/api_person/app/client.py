
import grpc
import os
from protobuf import person_pb2, person_pb2_grpc

#channel = grpc.insecure_channel("localhost:50051")
api_person_host = os.getenv("API_PERSON_HOST", "localhost")

channel = grpc.insecure_channel(f"{api_person_host}:50051", options=(('grpc.enable_http_proxy', 0),))
stub = person_pb2_grpc.PersonServiceStub(channel)


# person = person_pb2.CreatePersonRequest(
#     first_name = "Kivi",
#     last_name = "sto",
#     company_name = "Wrong",
# )


# response = stub.CreatePerson(person) 
# print("resppp", response)


response3 = stub.GetPerson(person_pb2.GetPersonRequest(id=1))

print("resppp3\n", response3)

response2 = stub.GetAllPersons(person_pb2.Empty())
print("resppp2", response2)
