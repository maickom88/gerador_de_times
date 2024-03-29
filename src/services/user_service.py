from datetime import datetime

from fastapi import HTTPException

from urllib.parse import unquote

from src.enums.roles_enum import RolesEnum
from src.models.user_model import UserInput
from src.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def create(self, input: UserInput):
        user_exist = await self.verify_if_user_exist(email=input.email)
        if user_exist:
            entity = await self.repository.get_entity(email=input.email)
            entity.first_access = input.first_access
            return await self.repository.update(entity)
        return await self.repository.create(input)

    async def verify_if_user_exist(self, email: str) -> bool:
        entity = await self.repository.get_entity(email=email)
        if entity is not None:
            return True
        return False

    async def update_photo(self, photo: str, guid_user: str):
        user = await self.repository.get_entity_by_guid(guid_user)
        user.photo = photo
        await self.repository.update(user)

    async def update_name(self, guid: str, name: str):
        user = await self.repository.get_entity_by_guid(guid)
        user.name = name
        return await self.repository.update(user)

    async def notifier(self, token: str = None, name: str = None):
        if token is None:
            return
        from src.services.firebase_admin_service import FirebaseAdminService
        uid = FirebaseAdminService.get_uid(token)
        user = FirebaseAdminService.get_user(uid)
        entity = await self.repository.get_entity_by_email(user.email)
        if entity is not None:
            if entity.deleted_at is not None:
                entity.deleted_at = None
                await self.repository.update(entity)
            return entity
        new_user = UserInput()
        new_user.email = user.email
        if name is not None:
            new_user.name = name
        new_user.photo = user.photo_url
        return await self.create(new_user)

    async def update_status_account(self, guid_user: str, status: RolesEnum):
        if guid_user is None or len(guid_user) < 32:
            raise HTTPException(status_code=400, detail="Guid User is required")
        entity = await self.repository.get_entity_by_guid(guid=guid_user)
        entity.role = status
        return await self.repository.update(entity)

    async def update(self, input: UserInput):
        if input.guid is None or len(input.guid) < 32:
            raise HTTPException(status_code=400, detail="Guid User is required")
        entity = await self.repository.get_entity_by_guid(guid=input.guid)
        entity.name = input.name
        entity.photo = unquote(input.photo)
        entity.first_access = input.first_access
        return await self.repository.update(entity)

    async def update_name_user(self, guid: str, name: str):
        if guid is None or len(guid) < 32:
            raise HTTPException(status_code=400, detail="Guid User is required")
        entity = await self.repository.get_entity_by_guid(guid=guid)
        entity.name = name
        return await self.repository.update(entity)

    async def get_entity_by_guid(self, guid: str):
        if guid is not None:
            entity = await self.repository.get_entity_by_guid(guid=guid)
            if entity is None:
                raise HTTPException(status_code=404, detail="User not found")
            from src.repositories.purchase_repository import PurchaseRepository
            purchase_repository = PurchaseRepository()
            purchase = await purchase_repository.get_active_purchase_by_player(id_user=entity.id, deleted_at=None)
            if purchase is not None:
                if purchase.date_expired_purchase < datetime.now():
                    entity.role = RolesEnum.FREE
                    await self.repository.update(entity)
                else:
                    entity.role = RolesEnum.PREMIUM
                    await self.repository.update(entity)
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entity_by_email(self, email: str):
        if email is not None:
            entity = await self.repository.get_entity_by_email(email=email)
            if entity is None:
                raise HTTPException(status_code=404, detail="User not found")
            return entity
        else:
            raise HTTPException(status_code=400, detail="Guid is required")

    async def get_entities(self):
        return await self.repository.get_entities()

    async def delete_entity(self, guid: str):
        from src.services.firebase_admin_service import FirebaseAdminService
        entity = await self.get_entity_by_guid(guid)
        await self.repository.delete_entity(guid)
        result = FirebaseAdminService.delete_account(entity.email)
        return result
