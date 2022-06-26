from datetime import datetime
from sqlalchemy import Column, DateTime, BigInteger, String, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.settings.database import Base


class Notification(Base):
    __tablename__ = "tb_notifications"

    id = Column(BigInteger, primary_key=True)
    guid = Column(UUID, index=True)
    id_user = Column(BigInteger, ForeignKey("tb_users.id"))
    user = relationship("User", foreign_keys=[id_user], lazy="joined")
    title = Column(String)
    description = Column(String)
    is_read = Column(Boolean)
    navigate_to = Column(String)
    data = Column(JSON)

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
