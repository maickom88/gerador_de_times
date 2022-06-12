from typing import Optional
from pydantic import BaseModel, Field


class SkillInput(BaseModel):
    guid: Optional[str] = Field(None)
    strength: Optional[int] = Field(None)
    velocity: Optional[int] = Field(None)
    completion: Optional[int] = Field(None)
    dribble: Optional[int] = Field(None)

    class Config:
        orm_mode = True


class SkillOutput(BaseModel):
    guid: Optional[str] = Field(None)
    strength: Optional[int] = Field(None)
    velocity: Optional[int] = Field(None)
    completion: Optional[int] = Field(None)
    dribble: Optional[int] = Field(None)

    class Config:
        orm_mode = True
