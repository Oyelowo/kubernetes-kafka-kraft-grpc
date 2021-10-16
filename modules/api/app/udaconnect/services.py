import logging
from datetime import datetime, timedelta
import os
from typing import Dict, List

from app.udaconnect.schemas import (ConnectionSchema, LocationSchema,
                                    PersonSchema)
from google.protobuf.json_format import MessageToDict, MessageToJson

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


import grpc
from .protobuf import connection_pb2, connection_pb2_grpc, location_pb2, location_pb2_grpc, person_pb2

# channel = grpc.insecure_channel("localhost:50051", options=(('grpc.enable_http_proxy', 0),))
# stub = person_pb2_grpc.PersonServiceStub(channel)

API_LOCATION_HOST = os.getenv("API_LOCATION_HOST")
API_LOCATION_PORT = os.getenv("API_LOCATION_PORT")

API_PERSON_HOST = os.getenv("API_PERSON_HOST")
API_PERSON_PORT = os.getenv("API_PERSON_PORT")
class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5
    ):
        # """
        # Finds all Person who have been within a given distance of a given Person within a date range.

        # This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        # large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        # smoothly for a better user experience for API consumers?
        # """
    
        connection_channel = grpc.insecure_channel(f"{API_LOCATION_HOST}:{API_LOCATION_PORT}")
        #channel = grpc.insecure_channel(f"{api_person_host}:30002", options=(('grpc.enable_http_proxy', 0),))
        connection_stub = connection_pb2_grpc.ConnectionServiceStub(connection_channel)


        connection_request = connection_pb2.GetConnectionRequest(
            person_id = int(person_id),
            start_date = start_date, 
            end_date = end_date,
            meters = meters,
            )
        response = connection_stub.GetConnection(connection_request)

        print("resppppp3\n", response)
        return [MessageToDict(m, preserving_proto_field_name=True) for m in response.connections]


class LocationService:
    @staticmethod
    def retrieve(location_id):
        location_channel = grpc.insecure_channel(f"{API_LOCATION_HOST}:{API_LOCATION_PORT}")
        location_stub = location_pb2_grpc.LocationServiceStub(location_channel)
        
        location = location_pb2.GetLocationRequest(
            id =location_id,
        )
        retrieved_location = location_stub.GetLocation(location) 
        print("Getting locaation:", retrieved_location)
        return MessageToDict(retrieved_location, preserving_proto_field_name=True)


    @staticmethod
    def create(location: Dict):
        location_channel = grpc.insecure_channel(f"{API_LOCATION_HOST}:{API_LOCATION_PORT}")
        location_stub = location_pb2_grpc.LocationServiceStub(location_channel)
        
        location = location_pb2.CreateLocationnRequest(
            person_id = location["person_id"],
            longitude = location["longitude"],
            latitude = location["latitude"],
            creation_time = location["creation_time"]
        )
        new_location = location_stub.CreateLocation(location) 
        print("Creating new location", new_location)
        return MessageToDict(new_location, preserving_proto_field_name=True)


class PersonService:
    @staticmethod
    def create(stub, person):
        person = person_pb2.CreatePersonRequest(
            first_name = person["first_name"],
            last_name = person["last_name"],
            company_name = person["company_name"]
        )

        new_person = stub.CreatePerson(person) 
        print("Creating new person", new_person)
        return MessageToDict(new_person, preserving_proto_field_name=True)


    @staticmethod
    def retrieve(stub, person_id: int):
        person = stub.GetPerson(person_pb2.GetPersonRequest(id=person_id))
        print("Retrieving person", person)
        return MessageToDict(person, preserving_proto_field_name=True)

    @staticmethod
    def retrieve_all(stub):
        response = stub.GetAllPersons(person_pb2.Empty())
        print("Retrieving all persons", response)
        return  [MessageToDict(m, preserving_proto_field_name=True) for m in response.persons]

