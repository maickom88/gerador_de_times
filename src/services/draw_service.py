from random import shuffle
from typing import List
from fastapi import HTTPException

from src.models.draw_model import DrawInput
from src.services.team_service import TeamService


class DrawService:
    def __init__(self):
        self.teamService = TeamService()

    async def draw_players(self, input: DrawInput) -> List:
        teams = []
        players = input.players
        shuffle(players)
        if input.number_of_teams <= 0:
            raise HTTPException(status_code=400, detail="Number of times needs to be greater than 0")
        if (len(players) % input.number_of_teams) > 0:
            raise HTTPException(status_code=400, detail="A number of player pairs is required.")
        players_per_team = len(players) // input.number_of_teams
        # if players_per_team >= players_per_team:
        #    raise HTTPException(status_code=400, detail="It is not possible to draw players. number of low players")
        team = []
        index = 0
        while len(teams) < input.number_of_teams:
            if len(team) >= players_per_team:
                teams.append(team)
                team = []
            else:
                team.append(players[index])
                index = index + 1
        return teams
