import logging
from datetime import datetime, timedelta
from typing import Dict, List
from google.protobuf.json_format import MessageToJson, MessageToDict
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


# import grpc

from protobuf import person_pb2, connection_pb2_grpc, connection_pb2

# channel = grpc.insecure_channel("localhost:50051", options=(('grpc.enable_http_proxy', 0),))
# stub = person_pb2_grpc.PersonServiceStub(channel)


class ConnectionService:
    @staticmethod
    def find_contacts(stub, person_id: int, start_date: datetime, end_date: datetime, meters=5
    ):
        # """
        # Finds all Person who have been within a given distance of a given Person within a date range.

        # This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        # large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        # smoothly for a better user experience for API consumers?
        # """
    
        # channel = grpc.insecure_channel("localhost:50053")
        # #channel = grpc.insecure_channel(f"{api_person_host}:30002", options=(('grpc.enable_http_proxy', 0),))
        # # stub = person_pb2_grpc.PersonServiceStub(channel)
        # # location_stub = location_pb2_grpc.LocationServiceStub(channel)
        # connection_stub = connection_pb2_grpc.ConnectionServiceStub(channel)


        connection_request = connection_pb2.GetConnectionRequest(
            person_id = int(person_id),
            start_date = start_date, 
            end_date = end_date,
            meters = meters,
            )
        response = stub.GetConnection(connection_request)

        print("resppppp3\n", response)
        return [MessageToDict(m, preserving_proto_field_name=True) for m in response.connections]


class LocationService:
    @staticmethod
    def retrieve(location_id):
        # location, coord_text = (
        #     db.session.query(Location, Location.coordinate.ST_AsText())
        #     .filter(Location.id == location_id)
        #     .one()
        # )

        # # Rely on database to return text form of point to reduce overhead of conversion in app code
        # location.wkt_shape = coord_text
        return "location"

    @staticmethod
    def create(location: Dict):
        # validation_results: Dict = LocationSchema().validate(location)
        # if validation_results:
        #     logger.warning(f"Unexpected data format in payload: {validation_results}")
        #     raise Exception(f"Invalid payload: {validation_results}")

        # new_location = Location()
        # new_location.person_id = location["person_id"]
        # new_location.creation_time = location["creation_time"]
        # new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        # db.session.add(new_location)
        # db.session.commit()

        return "new_location"


class PersonService:
    @staticmethod
    def create(stub, person):
        person = person_pb2.CreatePersonRequest(
            first_name = person["first_name"],
            last_name = person["last_name"],
            company_name = person["company_name"]
        )

        new_person = stub.CreatePerson(person) 
        print("resppp", new_person)
        return MessageToDict(new_person, preserving_proto_field_name=True)


    @staticmethod
    def retrieve(stub, person_id: int):
        person = stub.GetPerson(person_pb2.GetPersonRequest(id=person_id))
        print("resppp3\n", person)
        return MessageToDict(person, preserving_proto_field_name=True)

    @staticmethod
    def retrieve_all(stub):
        response = stub.GetAllPersons(person_pb2.Empty())
        print("resppp2", response)
        # return  MessageToJson(response.persons[0], preserving_proto_field_name=True)
        return  [MessageToDict(m, preserving_proto_field_name=True) for m in response.persons]

