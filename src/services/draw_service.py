from random import shuffle
from typing import List
from fastapi import HTTPException

from src.models.draw_model import DrawInput
from src.models.player_model import PlayerOutput
from src.services.team_service import TeamService


class DrawService:
    def __init__(self):
        self.teamService = TeamService()

    async def draw_players(self, input: DrawInput) -> List:
        if input.balance_teams:
            return await self.draw_players_premium(input)
        teams = []
        players = input.players
        position_name = 'Goleiro'.upper()
        shuffle(players)
        if input.number_of_teams <= 0:
            raise HTTPException(status_code=400, detail="Number of times needs to be greater than 0")
        if (len(players) % input.number_of_teams) > 0:
            raise HTTPException(status_code=400, detail="A number of player pairs is required.")
        players_per_team = len(players) // input.number_of_teams
        goalkeepers = list(filter(lambda player: player.position.name.upper() == position_name, players))

        if len(goalkeepers) == input.number_of_teams:
            players = [item for item in players if not item.position.name.upper() == position_name]
            players_per_team -= len(goalkeepers)
        team = []
        index = 0

        while len(teams) < input.number_of_teams:
            if len(team) >= players_per_team:
                teams.append({"team": team})
                team = []
            else:
                team.append(players[index])
                index = index + 1
        if len(goalkeepers) == input.number_of_teams:
            for number in range(input.number_of_teams):
                teams[number]["team"].append(goalkeepers[number])
        return {"teams": teams}

    @staticmethod
    def getPerformance(player: PlayerOutput):
        total = (player.skills.strength +
                 player.skills.velocity +
                 player.skills.completion +
                 player.skills.dribble)
        return total

    async def draw_players_premium(self, input: DrawInput) -> List:
        teams = []
        players = input.players
        position_name = 'Goleiro'.upper()
        shuffle(players)
        if input.number_of_teams <= 0:
            raise HTTPException(status_code=400, detail="Number of times needs to be greater than 0")
        if (len(players) % input.number_of_teams) > 0:
            raise HTTPException(status_code=400, detail="A number of player pairs is required.")
        players_per_team = len(players) // input.number_of_teams
        goalkeepers = list(filter(lambda player: player.position.name.upper() == position_name, players))

        if len(goalkeepers) == input.number_of_teams:
            players = [item for item in players if not item.position.name.upper() == position_name]
            players_per_team -= len(goalkeepers)
        players.sort(reverse=True, key=self.getPerformance)

        for index in range(input.number_of_teams):
            teams.append({"team": []})

        index = 1
        for player in players:
            teams[(index-1)]["team"].append(player)
            if index >= input.number_of_teams:
                index = 1
            else:
                index += 1

        if len(goalkeepers) == input.number_of_teams:
            for number in range(input.number_of_teams):
                teams[number]["team"].append(goalkeepers[number])
        return {"teams": teams}
