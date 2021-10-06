from datetime import datetime

from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema,
)
from app.udaconnect.services import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO:
# 1.
# Subscribe to kafka location topic and dequeue location data from kafka
# Store locaton data

# 2.
# Create a Connection server that serves connection to udaconnect api services


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
