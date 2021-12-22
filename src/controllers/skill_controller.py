from typing import List
from fastapi import APIRouter

from src.models.skiil_model import SkillOutput, SkillInput
from src.services.skill_service import SkillService
from src.settings.logger import logger

router = APIRouter()
skill_router = {
    "router": router,
    "prefix": "/skill",
    "tags": ["Skill"],
}


@router.get(path="", response_model=List[SkillOutput])
async def get_skills():
    logger.info("Starting request to get_skills")
    service = SkillService()
    return await service.get_entities()


@router.get(path="/{guid}", response_model=SkillOutput)
async def get_skill(guid: str):
    logger.info("Starting request to get_skill")
    service = SkillService()
    return await service.get_entity_by_guid(guid)


@router.post(path="", response_model=SkillOutput, status_code=201)
async def register_skill(skill: SkillInput):
    logger.info("Starting request to register_skill")
    service = SkillService()
    return await service.create(skill)


@router.put(path="", response_model=SkillOutput, status_code=201)
async def update_skill(skill: SkillInput):
    logger.info("Starting request to update_skill")
    service = SkillService()
    return await service.update(skill)


@router.delete(path="/{guid}", status_code=204)
async def delete_skill(guid: str):
    logger.info("Starting request to delete_skill")
    service = SkillService()
    return await service.delete_entity(guid)
