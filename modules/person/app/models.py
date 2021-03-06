from __future__ import annotations

from sqlalchemy import Column, Integer, String, func
from sqlalchemy.dialects import postgresql

from config import db  # noqa

UUID = postgresql.UUID(as_uuid=True)

class Person(db.Model):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    
    @staticmethod
    def get_max_id(session) -> int:
        row = session.query(func.max(Person.id)).first()
        return row[0] if row[0] is not None else 0
        
    
    def jsonify(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company_name": self.company_name,
        }

