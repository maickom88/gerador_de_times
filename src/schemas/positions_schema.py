from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import UUID

from src.settings.database import Base
from sqlalchemy.sql.schema import ForeignKey


class Positions(Base):
    __tablename__ = "tb_positions"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    name = Column(String)
    description = Column(String)
    id_sport = Column(BigInteger, ForeignKey("tb_sports.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
