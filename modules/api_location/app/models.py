from __future__ import annotations

from config import db  # noqa
import uuid

from sqlalchemy import Column, Integer, String, create_engine

#engine = create_engine(‘mssql+pyodbc://server_name/database_name?driver=SQL Server?Trusted_Connection=yes’)

from sqlalchemy.dialects import postgresql

UUID = postgresql.UUID(as_uuid=True)

class Person(db.Model):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # uid = Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    
    def jsonify(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company_name": self.company_name,
        }

