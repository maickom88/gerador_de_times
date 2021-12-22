from typing import Optional
from pydantic import BaseModel, Field

from src.models.position_model import PositionOutput
from src.models.skiil_model import SkillOutput


class PlayerInput(BaseModel):
    guid: Optional[str] = Field(None)
    name: str = Field(None)
    photo: Optional[str] = Field(None)
    user_guid: str = Field(None)
    guid_skill: Optional[str] = Field(None)
    guid_position: Optional[str] = Field(None)

    class Config:
        orm_mode = True


class PlayerOutput(BaseModel):
    guid: Optional[str] = Field(None)
    name: str = Field(None)
    position: PositionOutput = Field(None)
    photo: Optional[str] = Field(None)
    skills: SkillOutput = Field(None)

    class Config:
        orm_mode = True
