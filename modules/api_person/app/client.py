
import grpc

from protobuf import person_pb2, person_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = person_pb2_grpc.PersonServiceStub(channel)


person = person_pb2.Person(
    #id = 7,
    first_name = "Oyelowo",
    last_name = "Oyedayo",
    company_name = "Blayz",
)


response = stub.CreatePerson(person)

print("resppp", response)


