# import time
# from typing import List

# from app.models import Person
# from app.services import  PersonService


# from protobuf import person_pb2, person_pb2_grpc


# class PersonServicer(person_pb2_grpc.PersonServiceServicer):
#     def CreatePerson(self, request, context):

#         request_value = {
#                  "id" : request.id,
#                 "first_name" : request.first_name,
#                 "last_name" : request.last_name,
#                 "company_name" : request.company_name,
#         }
#         print(request_value)
#         person = person_pb2.Person(**request_value)
#         new_person: Person = PersonService.create(person)

#         return new_person

#     def GetPerson(self, request, context):

#         request_value = {
#                  "id" : request.id,
#         }
#         print(request_value)
#         person = person_pb2.Person(**request_value)
#         new_person: Person = PersonService.retrieve(request.id)

#         return new_person

#     def GetAllPersons(self, request, context):

#         person = person_pb2.Person()
#         persons: List[Person] = PersonService.retrieve_all()

#         return persons




