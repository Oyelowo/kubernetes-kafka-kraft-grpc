# from __future__ import annotations

# from config import db  # noqa
# import uuid

# from sqlalchemy import Column, Integer, String, create_engine

# #engine = create_engine(‘mssql+pyodbc://server_name/database_name?driver=SQL Server?Trusted_Connection=yes’)

# from sqlalchemy.dialects import postgresql

# UUID = postgresql.UUID(as_uuid=True)

# class Person(db.Model):
#     __tablename__ = "person"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     # uid = Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)
#     company_name = Column(String, nullable=False)
    
#     def jsonify(self):
#         return {
#             "id": self.id,
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             "company_name": self.company_name,
#         }



from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry.point import Point
from sqlalchemy import (BigInteger, Column, Date, DateTime, ForeignKey,
                        Integer, String)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.hybrid import hybrid_property

from config import db  # noqa


class Location(db.Model):
    __tablename__ = "location"

    id = Column(BigInteger, primary_key=True)
    person_id = Column(Integer, nullable=False)
    coordinate = Column(Geometry("POINT"), nullable=False)
    creation_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    _wkt_shape: str = None

    @property
    def wkt_shape(self) -> str:
        # Persist binary form into readable text
        if not self._wkt_shape:
            point: Point = to_shape(self.coordinate)
            # normalize WKT returned by to_wkt() from shapely and ST_AsText() from DB
            self._wkt_shape = point.to_wkt().replace("POINT ", "ST_POINT")
        return self._wkt_shape

    @wkt_shape.setter
    def wkt_shape(self, v: str) -> None:
        self._wkt_shape = v

    def set_wkt_with_coords(self, lat: str, long: str) -> str:
        self._wkt_shape = f"ST_POINT({lat} {long})"
        return self._wkt_shape

    @hybrid_property
    def longitude(self) -> str:
        coord_text = self.wkt_shape
        return coord_text[coord_text.find(" ") + 1 : coord_text.find(")")]

    @hybrid_property
    def latitude(self) -> str:
        coord_text = self.wkt_shape
        return coord_text[coord_text.find("(") + 1 : coord_text.find(" ")]

    def jsonify(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "creation_time": str(self.creation_time),
        }


@dataclass
class Connection:
    person: Any
    location: Location
    # person: Person

    def jsonify(self):
        return {
            "location": self.location,
            "person": self.person,
        }

