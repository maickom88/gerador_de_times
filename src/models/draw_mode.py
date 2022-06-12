from typing import List
from pydantic import BaseModel, Field

from src.models.player_model import PlayerOutput


class DrawOutput(BaseModel):
    team: List[PlayerOutput] = Field(None)

    class Config:
        orm_mode = True
