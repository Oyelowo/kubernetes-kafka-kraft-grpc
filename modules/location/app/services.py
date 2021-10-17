import logging
import os
from datetime import datetime, timedelta
from typing import Dict, List

import grpc
from geoalchemy2.functions import ST_AsText, ST_Point
from google.protobuf.json_format import MessageToDict, MessageToJson
from sqlalchemy.sql import text

from config import db
from models import Connection, Location
from protobuf import person_pb2, person_pb2_grpc

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api-location")

import json

from flask import Flask, Response, g, jsonify, request


def create_order(order_data):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(order_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("items", kafka_data)


#channel = grpc.insecure_channel("localhost:50051")
API_PERSON_HOST = os.getenv("API_PERSON_HOST")
API_PERSON_PORT = os.getenv("API_PERSON_PORT")

# port 30002 has been mapped in the to from guest to host in the VM with vagrant
# Host: 192.168.50.4 or localhost
channel = grpc.insecure_channel(f"{API_PERSON_HOST}:{API_PERSON_PORT}")
#channel = grpc.insecure_channel(f"{api_person_host}:30002", options=(('grpc.enable_http_proxy', 0),))
stub = person_pb2_grpc.PersonServiceStub(channel)
class PersonService:
    @staticmethod
    def retrieve_all():
        response = stub.GetAllPersons(person_pb2.Empty())
        print("Successfully fetches all persons", response)
        return  [MessageToDict(p, preserving_proto_field_name=True) for p in response.persons]
        # return [{'id': 5, 'first_name': 'Taco', 'last_name': 'Fargo', 'company_name': 'Alpha Omega Upholstery'}, {'id': 6, 'first_name': 'Frank', 'last_name': 'Shader', 'company_name': 'USDA'}, {'id': 1, 'first_name': 'Pam', 'last_name': 'Trexler', 'company_name': 'Hampton, Hampton and McQuill'}, {'id': 8, 'first_name': 'Paul', 'last_name': 'Badman', 'company_name': 'Paul Badman & Associates'}, {'id': 9, 'first_name': 'Otto', 'last_name': 'Spring', 'company_name': 'The Chicken Sisters Restaurant'}]
    
    @staticmethod
    def retrieve(person_id):
        person = stub.GetPerson(person_pb2.GetPersonRequest(id=person_id))
        print("Successfully fetches user", person)
        return  MessageToDict(person, preserving_proto_field_name=True)




class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5
    ):
        """
        Finds all Person who have been within a given distance of a given Person within a date range.

        This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        smoothly for a better user experience for API consumers?
        """
        locations: List = db.session.query(Location).filter(
            Location.person_id == person_id
        ).filter(Location.creation_time < end_date).filter(
            Location.creation_time >= start_date
        ).all()
        
        # NOTE: 
        # This was the original implementation but doesn't seem optimal as we are 
        # trying to fetch all users from the database even though we will only need a fraction
        # of that. Below, each user data is fetched individually from the Person service, so
        # we only get what we use or need
        
        # Cache all users in memory for quick lookup
        # person_map = {person["id"]: person for person in PersonService.retrieve_all()}

        # Prepare arguments for queries
        data = []
        for location in locations:
            data.append(
                {
                    "person_id": person_id,
                    "longitude": location.longitude,
                    "latitude": location.latitude,
                    "meters": meters,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": (end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
                }
            )

        query = text(
            """
        SELECT  person_id, id, ST_X(coordinate), ST_Y(coordinate), creation_time
        FROM    location
        WHERE   ST_DWithin(coordinate::geography,ST_SetSRID(ST_MakePoint(:latitude,:longitude),4326)::geography, :meters)
        AND     person_id != :person_id
        AND     TO_DATE(:start_date, 'YYYY-MM-DD') <= creation_time
        AND     TO_DATE(:end_date, 'YYYY-MM-DD') > creation_time;
        """
        )
        result= []
        for line in tuple(data):
            for (
                exposed_person_id,
                location_id,
                exposed_lat,
                exposed_long,
                exposed_time,
            ) in db.engine.execute(query, **line):
                location = Location(
                    id=location_id,
                    person_id=exposed_person_id,
                    creation_time=exposed_time,
                )
                location.set_wkt_with_coords(exposed_lat, exposed_long)

                result.append(
                    Connection(
                        person=PersonService.retrieve(exposed_person_id), location=location,
                    )
                )

        return result


class LocationService:
    @staticmethod
    def retrieve(location_id: int) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        new_location.id = Location.get_max_id(db.session) + 1
        db.session.add(new_location)
        db.session.commit()

        return new_location

