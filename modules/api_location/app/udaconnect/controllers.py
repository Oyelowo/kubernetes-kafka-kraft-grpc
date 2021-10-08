from datetime import datetime
from kafka import KafkaProducer
from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema,
)
from app.udaconnect.services import LocationService, create_order
from flask import Flask, jsonify, request, g, Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
import json

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


@api.route("/orders")
class LocationResource1(Resource):
    # @accepts(schema=LocationSchema)
    # @responds(schema=LocationSchema)
    def post(self):
        request_body = request.get_json()
        print("before")
        kafka_data = json.dumps(request_body).encode()
        TOPIC_NAME = 'topic-a'
        KAFKA_SERVER = 'localhost:8001'
        kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
        kafka_producer.send("test", kafka_data)
        # result = create_order(request_body)
        print("after")
        return Response(status=202)



@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        location: Location = LocationService.create(request.get_json())
        return location

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location
