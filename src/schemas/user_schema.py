from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger, Enum, Boolean
from sqlalchemy.dialects.postgresql import UUID

from src.enums.roles_enum import RolesEnum
from src.settings.database import Base


class User(Base):
    __tablename__ = "tb_users"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    name = Column(String)
    email = Column(String)
    first_access = Column(Boolean, default=True)
    photo = Column(String)
    role = Column(Enum(RolesEnum), default=RolesEnum.FREE)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
