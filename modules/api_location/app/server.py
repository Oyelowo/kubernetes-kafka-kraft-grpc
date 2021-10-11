from datetime import datetime
from typing import List
from kafka import KafkaProducer
from app.models import Location
from app.schemas import (
    LocationSchema,
)
from app.services import LocationService, create_order, ConnectionService
from flask import Flask, jsonify, request, g, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
import json

from concurrent import futures
import os
import grpc
from modules.api_location.app.models import Connection

from protobuf import location_pb2, location_pb2_grpc
from config import create_app

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO:
# 1.
# Subscribe to kafka location topic and dequeue location data from kafka
# Store locaton data

# 2.
# Create a Connection server that serves connection to udaconnect api services
app = Flask(__name__)

def create_order(order_data):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(order_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("items", kafka_data)

@app.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'topic-a'
    KAFKA_SERVER = 'localhost:9093'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer


# @api.route("/orders")
# class LocationResource1(Resource):
#     # @accepts(schema=LocationSchema)
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



class ConnectionServicer(location_pb2_grpc.ConnectionServiceServicer):
    def GetConnection(self, request, context):

        request_value = {
                "person_id" : request.person_id,
                "start_date" : request.start_date,
                "end_date" : request.end_date,
                "meters": request.meters,
        }
        connections_db: List[Connection] = ConnectionService.find_contacts(request_value)
        connection_response = location_pb2.ConnectionResponse()
        connection_response.connections.extend([location_pb2.Connection(**c.jsonify()) for c in connections_db])

        return connection_response

 

class Server:
    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        location_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)
        create_app(os.getenv("FLASK_ENV") or "test")
        server.add_insecure_port('[::]:50052')
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    Server.run()
