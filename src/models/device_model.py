from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

from src.enums.plataform_enum import PlatformEnum
from src.models.user_model import UserOutput


class DeviceInput(BaseModel):
    guid: Optional[str] = Field(None)
    guid_user: Optional[str] = Field(None)
    token: str = Field(None)
    platform: PlatformEnum = Field(None)

    class Config:
        orm_mode = True


class DeviceOutput(BaseModel):
    guid: Optional[str] = Field(None)
    user: UserOutput = Field(None)
    token: Optional[str] = Field(None)
    platform: PlatformEnum = Field(None)

    class Config:
        orm_mode = True
