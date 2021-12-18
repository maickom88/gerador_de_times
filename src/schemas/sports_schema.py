from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger, Boolean
from sqlalchemy.dialects.postgresql import UUID

from src.settings.database import Base


class Sports(Base):
    __tablename__ = "tb_sports"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    name = Column(String)
    description = Column(String)
    photo = Column(String)
    tutorial = Column(String)
    icon = Column(String)
    is_available = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
