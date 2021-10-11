from datetime import datetime
import json
import os
from google.protobuf.json_format import MessageToJson
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import ConnectionService, LocationService, PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa
import grpc

from protobuf import person_pb2, person_pb2_grpc

api_person_host = os.getenv("API_PERSON_HOST", "localhost")

channel = grpc.insecure_channel(f"{api_person_host}:50051", options=(('grpc.enable_http_proxy', 0),))
stub = person_pb2_grpc.PersonServiceStub(channel)



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
    
from flask import Flask, jsonify

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
        # all_persons = stub.GetAllPersons(person_pb2.Empty())
        print("resppp2", all_persons)

        return all_persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
   # @responds(schema=PersonSchema)
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
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        # TODO: Get connection data from location service via GRPC
        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results
