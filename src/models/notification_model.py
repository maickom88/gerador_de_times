from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class NotificationInput(BaseModel):
    guid: Optional[str] = Field(None)
    guid_user: Optional[str] = Field(None)
    title: str = Field(None)
    description: Optional[str] = Field(None)
    navigate_to: Optional[str] = Field(None)
    is_read: Optional[bool] = Field(None)
    data: Optional[dict] = Field(None)

    class Config:
        orm_mode = True


class NotificationOutput(BaseModel):
    guid: Optional[str] = Field(None)
    title: str = Field(None)
    description: Optional[str] = Field(None)
    navigate_to: Optional[str] = Field(None)
    is_read: Optional[bool] = Field(None)
    data: Optional[dict] = Field(None)
    created_at: datetime = Field(None)

    class Config:
        orm_mode = True
