import logging
from datetime import datetime, timedelta
from typing import Dict, List

from app import db
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

from modules.api.app.protobuf.person_pb2 import Person

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")


import grpc

from app.protobuf import person_pb2, person_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = person_pb2_grpc.PersonServiceStub(channel)


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
        # locations: List = db.session.query(Location).filter(
        #     Location.person_id == person_id
        # ).filter(Location.creation_time < end_date).filter(
        #     Location.creation_time >= start_date
        # ).all()

        # # Cache all users in memory for quick lookup
        # person_map: Dict[str, Person] = {person.id: person for person in PersonService.retrieve_all()}

        # # Prepare arguments for queries
        # data = []
        # for location in locations:
        #     data.append(
        #         {
        #             "person_id": person_id,
        #             "longitude": location.longitude,
        #             "latitude": location.latitude,
        #             "meters": meters,
        #             "start_date": start_date.strftime("%Y-%m-%d"),
        #             "end_date": (end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
        #         }
        #     )

        # query = text(
        #     """
        # SELECT  person_id, id, ST_X(coordinate), ST_Y(coordinate), creation_time
        # FROM    location
        # WHERE   ST_DWithin(coordinate::geography,ST_SetSRID(ST_MakePoint(:latitude,:longitude),4326)::geography, :meters)
        # AND     person_id != :person_id
        # AND     TO_DATE(:start_date, 'YYYY-MM-DD') <= creation_time
        # AND     TO_DATE(:end_date, 'YYYY-MM-DD') > creation_time;
        # """
        # )
        # result: List[Connection] = []
        # for line in tuple(data):
        #     for (
        #         exposed_person_id,
        #         location_id,
        #         exposed_lat,
        #         exposed_long,
        #         exposed_time,
        #     ) in db.engine.execute(query, **line):
        #         location = Location(
        #             id=location_id,
        #             person_id=exposed_person_id,
        #             creation_time=exposed_time,
        #         )
        #         location.set_wkt_with_coords(exposed_lat, exposed_long)

        #         result.append(
        #             Connection(
        #                 person=person_map[exposed_person_id], location=location,
        #             )
        #         )

        return "result"


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
    def create(person) -> Person:
        person = person_pb2.CreatePersonRequest(
            first_name = person["first_name"],
            last_name = person["last_name"],
            company_name = person["company_name"]
        )

        new_person = stub.CreatePerson(person) 
        print("resppp", new_person)


        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = stub.GetPerson(person_pb2.GetPersonRequest(id=person_id))
        print("resppp3\n", person)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        all_persons = stub.GetAllPersons(person_pb2.Empty())
        print("resppp2", all_persons)
        return all_persons

