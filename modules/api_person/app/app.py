from concurrent import futures
import os

from flask import Flask, jsonify
from flask_cors import CORS

import grpc

from protobuf import person_pb2_grpc
# from .protobuf import person_pb2, person_pb2_grpc

from config import config_by_name, db




from typing import List

from models import Person
from services import  PersonService

from protobuf import person_pb2, person_pb2_grpc


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def CreatePerson(self, request, context):

        request_value = {
                 #"id" : request.id,
                "first_name" : request.first_name,
                "last_name" : request.last_name,
                "company_name" : request.company_name,
        }
        print(request_value)
        person = person_pb2.Person(**request_value)
        new_person: Person = PersonService.create(request_value)

        return person

    def GetPerson(self, request, context):

        request_value = {
                 "id" : request.id,
        }
        print(request_value)
        person = person_pb2.Person(**request_value)
        new_person: Person = PersonService.retrieve(request.id)

        return new_person

    def GetAllPersons(self, request, context):

        person = person_pb2.Person()
        persons: List[Person] = PersonService.retrieve_all()

        return persons


from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy



def create_app(env=None):
    from config import config_by_name

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    #api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development
    db.init_app(app)

    # @app.route("/health")
    # def health():
    #     return jsonify("healthy")

    return app



class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)
        app = create_app(os.getenv("FLASK_ENV") or "test")
        # app.run(debug=True)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    Server.run()
