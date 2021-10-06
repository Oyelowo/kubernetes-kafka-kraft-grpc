
import grpc

from protobuf import person_pb2, person_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = person_pb2_grpc.PersonServiceStub(channel)


# person = person_pb2.Person(
#     #id = 7,
#     first_name = "Oyelowo2",
#     last_name = "Oyedayo2",
#     company_name = "Blayz2",
# )


# response = stub.CreatePerson(person) 
# print("resppp", response)


response3 = stub.GetPerson(person_pb2.GetPersonRequest(id=1))

print("resppp3", response3)

response2 = stub.GetAllPersons(person_pb2.Empty())
print("resppp2", response2)
