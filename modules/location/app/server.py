import json
import os
from concurrent import futures
from datetime import datetime

import grpc
from flask import Flask, Response, g, jsonify, request
from kafka import KafkaConsumer, KafkaProducer

from config import create_app
from protobuf import (connection_pb2, connection_pb2_grpc, location_pb2,
                      location_pb2_grpc, person_pb2, person_pb2_grpc)
from services import ConnectionService, LocationService

# from schemas import LocationSchema



DATE_FORMAT = "%Y-%m-%d"

KAFKA_HOST = os.getenv("KAFKA_HOST")
KAFKA_PORT = os.getenv("KAFKA_PORT")
    

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
        producer = KafkaProducer(bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}")
        data = {**request.get_json(), "creation_time": datetime.now().isoformat(timespec='seconds')}
        kafka_data = json.dumps(data).encode()
        
        print("Sending data to kafka Via GRPC", kafka_data)
        producer.send('location', kafka_data)
        producer.flush()

        # new_location = LocationService.create(request_value)
        # This shouldn't return ID this way as it's sending data to the queue as DB would't have yet created the ID
        # Would probably be better to return an empty value?
        location = location_pb2.Location(id=999, **request_value)

        return location

    def GetLocation(self, request, context):
        request_value = {
                "id" : request.id,
        }
        print(request_value)
        location_db = LocationService.retrieve(int(request.id))
        print("Successfuly gets location from locaation service,", location_db)
        return location_pb2.Location(**location_db.jsonify())

 


def consume_location():
    location_topic = "location"
    consumer = KafkaConsumer(
        location_topic,
        bootstrap_servers=[f"{KAFKA_HOST}:{KAFKA_PORT}"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="location_consumer_group",
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    for msg in consumer:
        print("msg", msg.value)
        LocationService.create(msg.value)
        print("Successfully stores location")

class Server:
    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)
        location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
        create_app(os.getenv("FLASK_ENV") or "test")
        server.add_insecure_port('[::]:50051')
        
        server.start()
        consume_location()
        server.wait_for_termination()


if __name__ == '__main__':
    Server.run()

