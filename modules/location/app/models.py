# from __future__ import annotations

# from config import db  # noqafrom __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely.geometry.point import Point
from sqlalchemy import BigInteger, Column, DateTime, Integer, func
from sqlalchemy.ext.hybrid import hybrid_property

from config import db  # noqa


class Location(db.Model):
    __tablename__ = "location"

    id = Column(BigInteger, primary_key=True)
    person_id = Column(Integer, nullable=False)
    coordinate = Column(Geometry("POINT"), nullable=False)
    creation_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    _wkt_shape: str = None
    
    @staticmethod
    def get_max_id(session) -> int:
        row = session.query(func.max(Location.id)).first()
        return row[0] if row[0] is not None else 0
        

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
            "creation_time": self.creation_time.isoformat(timespec='seconds'),
        }


@dataclass
class Connection:
    person: Any
    location: Location

    def jsonify(self):
        return {
            "location": self.location,
            "person": self.person,
        }

