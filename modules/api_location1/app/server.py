# from datetime import datetime
# from typing import List
# from kafka import KafkaProducer
# from models import Location
# from schemas import (
#     LocationSchema,
# )
# from flask import Flask, jsonify, request, g, Response
# import json

# from concurrent import futures
# import os
# import grpc

# from models import Connection
# from services import LocationService, ConnectionService

# from protobuf import connection_pb2, connection_pb2_grpc, location_pb2, location_pb2_grpc
# from config import create_app

# DATE_FORMAT = "%Y-%m-%d"



# # TODO:
# # 1.
# # Subscribe to kafka location topic and dequeue location data from kafka
# # Store locaton data

# # 2.
# # Create a Connection server that serves connection to udaconnect api services

# def create_location(order_data):
#     """
#     This is a stubbed method of retrieving a resource. It doesn't actually do anything.
#     """
#     # Turn order_data into a binary string for Kafka
#     kafka_data = json.dumps(order_data).encode()
#     # Kafka producer has already been set up in Flask context
#     kafka_producer = g.kafka_producer
#     kafka_producer.send("items", kafka_data)

# #@app.before_request
# def before_request():
#     # Set up a Kafka producer
#     TOPIC_NAME = 'topic-a'
#     KAFKA_SERVER = 'localhost:9093'
#     producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
#     # Setting Kafka to g enables us to use this
#     # in other parts of our application
#     g.kafka_producer = producer


# # @api.route("/orders")
# # class LocationResource1(Resource):
# #     # @accepts(schema=LocationSchema)
# #     # @responds(schema=LocationSchema)
# #     def post(self):
# #         request_body = request.get_json()
# #         print("before")
# #         kafka_data = json.dumps(request_body).encode()
# #         TOPIC_NAME = 'topic-a'
# #         KAFKA_SERVER = 'localhost:8001'
# #         kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
# #         kafka_producer.send("test", kafka_data)
# #         # result = create_order(request_body)
# #         print("after")
# #         return Response(status=202)



# class ConnectionServicer(connection_pb2_grpc.ConnectionServiceServicer):
#     def GetConnection(self, request, context):
#         request_value = {
#                 "person_id" : request.person_id,
#                 "start_date" : request.start_date,
#                 "end_date" : request.end_date,
#                 "meters": request.meters,
#         }
#         print(request_value)
#         connections_db: List[Connection] = ConnectionService.find_contacts(request_value)
#         connection_response = connection_pb2.ConnectionResponse()
#         connection_response.connections.extend([connection_pb2.Connection(**c.jsonify()) for c in connections_db])

#         return connection_response

 

# class Server:
#     @staticmethod
#     def run():
#         server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#         # location_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)
#         connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)
#         create_app(os.getenv("FLASK_ENV") or "test")
#         server.add_insecure_port('[::]:50051')
#         server.start()
#         server.wait_for_termination()


# if __name__ == '__main__':
#     Server.run()


from concurrent import futures
import os
import grpc
from typing import List

from config import  create_app
from models import Person
from services import  PersonService
from protobuf import person_pb2, person_pb2_grpc


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def GetPerson(self, request, context):

        request_value = {
                 "id" : request.id,
                "first_name" : request.first_name,
                "last_name" : request.last_name,
                "company_name" : request.company_name,
        }
        print(request_value)
        person = person_pb2.Person(       
                id = request.id,
                first_name = "request.first_name",
                last_name = "request.last_name",
                company_name = "request.company_name")
        print("Get it person,", person)
        return person


class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)
        create_app(os.getenv("FLASK_ENV") or "test")
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    Server.run()
