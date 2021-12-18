import os
from logging.config import fileConfig

from dotenv.main import load_dotenv
from sqlalchemy import create_engine

from alembic import context

from src.settings.database import Base
from src.schemas import help_schema, help_like_schema, user_schema, \
    information_schema, location_schema, portfolio_schema, terms_of_conditions_schema, \
    service_schema, service_value_schema, type_service_schema, available_schema, \
    achievements_schema, sub_category_schema, problem_schema

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata


def get_url() -> str:
    return os.getenv("DB_URL")


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """

    # url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    load_dotenv()
    connectable = create_engine(get_url())

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
