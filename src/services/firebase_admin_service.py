import json

import firebase_admin
from firebase_admin import auth, credentials

from src.errors.login_error import LoginException
from src.services.user_service import UserService
from src.settings.environment import env
from src.settings.logger import logger


class FirebaseAdminService:
    cred = credentials.Certificate(json.loads(env.firebase_account_credential()))
    _firebase_app = firebase_admin.initialize_app(cred)

    def __init__(self):
        self.user_service = UserService()

    @staticmethod
    def validate_token(id_token: str) -> bool:
        try:
            decoded_token = auth.verify_id_token(id_token)
            if decoded_token.get("uid"):
                email = decoded_token.get("email")
                logger.info(f"Request authorized by {email}")
                return True
            return False
        except Exception as e:
            raise LoginException(detail=f"Invalid token: {e}")

    @staticmethod
    def get_uid(token: str) -> bool:
        try:
            decoded_token = auth.verify_id_token(token)
            if decoded_token.get("uid"):
                return decoded_token.get("uid")
            return False
        except Exception as e:
            raise LoginException(detail=f"Invalid token: {e}")

    @staticmethod
    def get_user(uid: str):
        return auth.get_user(uid)

    @staticmethod
    def revoke_refresh_tokens(uid: str):
        auth.revoke_refresh_tokens(uid)

    async def delete_user(self, user_guid):
        user = await self.user_service.get_entity_by_guid(user_guid)
        if user.firebase_uid:
            auth.delete_user(user.firebase_uid)
        return True
