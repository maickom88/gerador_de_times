from typing import Optional
from pydantic import BaseModel, Field

from src.enums.roles_enum import RolesEnum


class UserInput(BaseModel):
    guid: Optional[str] = Field(None)
    email: str = Field(None)
    name: str = Field(None)
    first_access: bool = Field(None)
    photo: str = Field(None)
    role: RolesEnum = Field(None)

    class Config:
        orm_mode = True


class UserOutput(BaseModel):
    guid: Optional[str] = Field(None)
    email: str = Field(None)
    name: str = Field(None)
    document: str = Field(None)
    first_access: bool = Field(None)
    photo: str = Field(None)
    role: RolesEnum = Field(None)

    class Config:
        orm_mode = True
