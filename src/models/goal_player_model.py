from typing import Optional
from pydantic import BaseModel, Field

from src.models.player_model import PlayerOutput


class GoalPlayerOutput(BaseModel):
    goals: Optional[int] = Field(None)
    player: PlayerOutput = Field(None)

    class Config:
        orm_mode = True
