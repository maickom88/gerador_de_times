from typing import Optional
from pydantic import BaseModel, Field


class SportInput(BaseModel):
    guid: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    photo: Optional[str] = Field(None)
    tutorial:  Optional[str] = Field(None)
    icon:  Optional[str] = Field(None)
    is_available:  Optional[bool] = Field(None)

    class Config:
        orm_mode = True


class SportOutput(BaseModel):
    guid: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    photo: Optional[str] = Field(None)
    tutorial:  Optional[str] = Field(None)
    icon:  Optional[str] = Field(None)
    is_available:  Optional[bool] = Field(None)

    class Config:
        orm_mode = True
