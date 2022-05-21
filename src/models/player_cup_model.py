from pydantic import BaseModel, Field


class PlayerCupOutput(BaseModel):
    total_number_of_cup_participations: int = Field(None)

    class Config:
        orm_mode = True


class PlayerWinnerOutput(BaseModel):
    total_number_of_winner_cup: int = Field(None)

    class Config:
        orm_mode = True
