import json
import os
from concurrent import futures
from datetime import datetime

import grpc
from kafka import KafkaProducer

from config import create_app
from protobuf import (location_pb2, location_pb2_grpc)


DATE_FORMAT = "%Y-%m-%d"

KAFKA_HOST = os.getenv("KAFKA_HOST")
KAFKA_PORT = os.getenv("KAFKA_PORT")


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def CreateLocation(self, request, context):
        request_value = {
                "person_id" : request.person_id,
                "longitude" : request.longitude,
                "latitude" : request.latitude,
                # "creation_time" : request.creation_time,
        }
        print(request_value)
        
        producer = KafkaProducer(bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}")
        data = {**request_value, "creation_time": datetime.now().isoformat(timespec='seconds')}
        kafka_data = json.dumps(data).encode()
        
        print("Sending data to kafka", kafka_data)
        producer.send('location', kafka_data)
        producer.flush()

        location = location_pb2.Empty()

        return location

 

class Server:
    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
        create_app(os.getenv("FLASK_ENV") or "test")
        server.add_insecure_port('[::]:50053')
        
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    Server.run()

