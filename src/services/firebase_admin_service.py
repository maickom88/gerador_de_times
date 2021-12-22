import json

import firebase_admin
from firebase_admin import auth, credentials, messaging
from firebase_admin.messaging import Notification

from src.errors.login_error import LoginException
from src.services.user_service import UserService
from src.settings.environment import env


class FirebaseAdminService:
    cred = credentials.Certificate(json.loads(env.firebase_account_credential()))
    _firebase_app = firebase_admin.initialize_app(cred)

    def __init__(self):
        self.user_service = UserService()

    @staticmethod
    def validate_token(id_token: str) -> bool:
        try:
            decoded_token = auth.verify_id_token(id_token)
            if decoded_token['uid']:
                return True
            return False
        except Exception as e:
            raise LoginException(detail=f"Invalid token: {e}")

    async def delete_user(self, user_guid):
        user = await self.user_service.get_entity_by_guid(user_guid)
        if user.firebase_uid:
            auth.delete_user(user.firebase_uid)

        return True

    async def send_multicast(self, notification, person_name=None, person_last_name=None):
        registration_tokens = await self.device_service.get_tokens(notification.id_user_target)
        if len(registration_tokens) > 0:
            message = messaging.MulticastMessage(
                notification=Notification(
                    title=notification.message,
                ),
                data={
                    "guid": str(notification.guid),
                    "android": "true",
                    "type": notification.type,
                    "person_name": str(person_name),
                    "person_last_name": str(person_last_name),
                    "message": notification.message,
                    "entity_name": str(notification.entity_name),
                    "guid_entity": str(notification.guid_entity),
                    "created_at": str(notification.created_at)
                },
                tokens=registration_tokens,
            )
            response = messaging.send_multicast(message)

            return response
        return
