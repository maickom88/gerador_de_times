import json
import os
from dotenv import load_dotenv

from src.settings.logger import logger


class Environment:
    def __init__(self):
        load_dotenv()
        self._ENV_API_HOST: str = os.getenv("HOST")
        self._ENV_API_PORT: str = os.getenv("PORT")
        self._ENV_IS_DEBUG: bool = os.getenv("DEBUG")

        self._ENV_SMTP_EMAIL: str = os.getenv("SMTP_EMAIL")
        self._ENV_SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD")

        self._ENV_DATABASE_URL: str = os.getenv("DB_URL")
        self._ENV_DATABASE_NAME: str = os.getenv("DB_NAME")
        self._ENV_DATABASE_ECHO: bool = os.getenv(
            "DB_ECHO", "0") == "1"

        self._ENV_FIREBASE_CONF: str = os.getenv("ENV_FIREBASE_CONF")
        self._ENV_FIREBASE_ACCOUNT_CREDENTIAL: str = os.getenv("ENV_FIREBASE_ACCOUNT_CREDENTIAL")

    def environment_validate(self):
        msg = []
        for k in self.__dict__:
            if self.__dict__[k] is None:
                msg.append(f"{k} is not configured in environment")

        try:
            json.loads(self._ENV_FIREBASE_CONF)
        except Exception as e:
            logger.error(f"Error on convert ENV_FIREBASE_CONF to dict: {e}")
            msg.append("Error on convert ENV_FIREBASE_CONF to dict")

        if len(msg) > 0:
            logger.error(f"Error in ENV, not configure: {msg}")
            raise EnvironmentError(msg)

    def api_host(self) -> str:
        return self._ENV_API_HOST

    def api_port(self) -> int:
        return int(self._ENV_API_PORT)

    def is_debug(self) -> bool:
        return bool(self._ENV_IS_DEBUG)

    def database_url(self) -> str:
        return self._ENV_DATABASE_URL

    def database_name(self) -> str:
        return self._ENV_DATABASE_NAME

    def database_echo(self) -> bool:
        return self._ENV_DATABASE_ECHO

    def firebase_config(self) -> dict:
        return json.loads(self._ENV_FIREBASE_CONF)

    def firebase_account_credential(self) -> str:
        return self._ENV_FIREBASE_ACCOUNT_CREDENTIAL

    def smtp_email(self) -> str:
        return self._ENV_SMTP_EMAIL

    def smtp_password(self) -> str:
        return self._ENV_SMTP_PASSWORD


env = Environment()
