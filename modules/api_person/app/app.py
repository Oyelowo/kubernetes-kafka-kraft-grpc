from concurrent import futures
import grpc

from protobuf import person_pb2_grpc


from typing import List

from models import Person
from services import  PersonService

from protobuf import person_pb2, person_pb2_grpc


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def CreatePerson(self, request, context):

        request_value = {
                "first_name" : request.first_name,
                "last_name" : request.last_name,
                "company_name" : request.company_name,
        }
        print(request_value)
        new_person: Person = PersonService.create(request_value)

        person = person_pb2.Person(**new_person.jsonify())

        return person

    def GetPerson(self, request, context):

        request_value = {
                 "id" : request.id,
        }
        print(request_value)
        new_person: Person = PersonService.retrieve(request.id)
        person = person_pb2.Person(**new_person.jsonify())
        print("Get it person,", person)
        return person

    def GetAllPersons(self, request, context):
        persons_db: List[Person] = PersonService.retrieve_all()
        persons = person_pb2.Persons()
        persons.persons.extend([person_pb2.Person(**p.jsonify()) for p in persons_db])
        
        return persons



class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    Server.run()
