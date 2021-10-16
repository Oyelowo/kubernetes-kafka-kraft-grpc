import json
import os
from concurrent import futures
from datetime import datetime

import grpc
from flask import Flask, Response, g, jsonify, request
from kafka import KafkaProducer

from config import create_app
from services import ConnectionService, LocationService

from protobuf import (connection_pb2, connection_pb2_grpc, location_pb2,
                       location_pb2_grpc, person_pb2, person_pb2_grpc)

# from schemas import LocationSchema



DATE_FORMAT = "%Y-%m-%d"



# TODO:
# 1.
# Subscribe to kafka location topic and dequeue location data from kafka
# Store locaton data

# 2.
# Create a Connection server that serves connection to udaconnect api services

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


# @api.route("/orders")
# class LocationResource1(Resource):
# #     # @accepts(schema=LocationSchema)
#     # @responds(schema=LocationSchema)
#     def post(self):
#         request_body = request.get_json()
#         print("before")
#         kafka_data = json.dumps(request_body).encode()
#         TOPIC_NAME = 'topic-a'
#         KAFKA_SERVER = 'localhost:8001'
#         kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
#         kafka_producer.send("test", kafka_data)
#         # result = create_order(request_body)
#         print("after")
#         return Response(status=202)


def format_date(date):
    return datetime.strptime(
            date, DATE_FORMAT
        )
class ConnectionServicer(connection_pb2_grpc.ConnectionServiceServicer):
    def GetConnection(self, request, context):
        request_value = {
                "person_id" : request.person_id,
                "start_date" : format_date(request.start_date),
                "end_date" : format_date(request.end_date),
                "meters": float(request.meters),
        }
        print(request_value)
        connections_db = ConnectionService.find_contacts(**request_value)
        connection_response = connection_pb2.ConnectionResponse()
        connection_response.connections.extend([connection_pb2.Connection(person=c.person, location=c.location.jsonify()) for c in connections_db])

        return connection_response
    
class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def CreateLocation(self, request, context):
        request_value = {
                "person_id" : request.person_id,
                "longitude" : request.longitude,
                "latitude" : request.latitude,
                "creation_time" : request.creation_time,
        }
        print(request_value)
        new_location = LocationService.create(request_value)

        location = location_pb2.Location(**new_location.jsonify())

        return location
    def GetConnection(self, request, context):
        request_value = {
                "id" : request.id,
        }
        print(request_value)
        location_db = LocationService.retrieve(**request_value)
        print("Successfuly gets location from locaation service,", location_db)
        return location_pb2.Location(**location_db.jsonify())

 

class Server:
    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)
        location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
        create_app(os.getenv("FLASK_ENV") or "test")
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    Server.run()

