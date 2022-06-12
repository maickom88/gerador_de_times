from typing import List

from fastapi import APIRouter, Depends

from src.authenticator.auth import get_token
from src.models.draw_mode import DrawOutput
from src.models.draw_model import DrawInput
from src.services.draw_service import DrawService
from src.settings.logger import logger

router = APIRouter()
draw_router = {
    "router": router,
    "prefix": "/draw",
    "tags": ["Draw"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="",  status_code=201)
async def register_draw(draw: DrawInput):
    logger.info("Starting request to register_draw")
    service = DrawService()
    return await service.draw_players(draw)

