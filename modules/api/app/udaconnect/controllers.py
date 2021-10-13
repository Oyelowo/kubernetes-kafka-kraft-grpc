import json
import os
from datetime import datetime
from typing import List, Optional

from app.udaconnect.schemas import (ConnectionSchema, LocationSchema,
                                    PersonSchema)
from app.udaconnect.services import (ConnectionService, LocationService,
                                     PersonService)
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from google.protobuf.json_format import MessageToJson

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa
import grpc
from protobuf import connection_pb2_grpc, person_pb2, person_pb2_grpc

api_person_host = os.getenv("API_PERSON_HOST", "localhost")
api_location_host = os.getenv("API_LOCATION_HOST", "localhost")

channel = grpc.insecure_channel(f"{api_person_host}:50052")
stub = person_pb2_grpc.PersonServiceStub(channel)

connection_channel = grpc.insecure_channel(f"{api_location_host}:50051")
connection_stub = connection_pb2_grpc.ConnectionServiceStub(connection_channel)

# TODO: This needs better exception handling


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self):
        request.get_json()
        # TODO: Send location data to Kafka Location topic
        location = LocationService.create(request.get_json())
        return location

    @responds(schema=LocationSchema)
    def get(self, location_id):
        # TODO: Get location data from location service via GRPC
        location = LocationService.retrieve(location_id)
        return location

@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self):
        payload = request.get_json()
        # TODO: Send Person payload to person service via GRPC
        new_person = PersonService.create(stub, payload)
        return str(new_person)

    @responds(schema=PersonSchema, many=True)
    def get(self):
        # TODO: Get all persons from person service via GRPC
        all_persons = PersonService.retrieve_all(stub)
        return all_persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id):
        # TODO: Get person from person service via GRPC
        person = PersonService.retrieve(stub, int(person_id))
        return person


@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        distance: Optional[int] = request.args.get("distance", 5)

        # TODO: Get connection data from location service via GRPC
        results = ConnectionService.find_contacts(
            person_id=int(person_id),
            start_date=request.args["start_date"],
            end_date=request.args["end_date"],
            meters=float(distance),
        )
        return results
