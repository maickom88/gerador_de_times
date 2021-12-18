import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from src.settings.environment import env

env.environment_validate()

engine = create_engine(
    env.database_url(),
    echo=env.database_echo()
)

Base = declarative_base()


def apply_migrations():
    command = "alembic upgrade head"
    os.system(command)
