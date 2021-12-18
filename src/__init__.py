from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette_context import plugins
from starlette_context.middleware import ContextMiddleware

from src.errors.base_error import ApiBaseException, generic_handler
from src.router.routers import get_routers
from src.settings.database import apply_migrations, engine


def init_app():
    app = _init_fastapi_app()
    return app


def _init_fastapi_app() -> FastAPI:
    app = FastAPI(
        **_get_app_args()
    )
    app = _config_app_events(app)
    app = _config_app_middlewares(app)
    app = _config_app_routers(app)
    app = _config_app_exceptions(app)
    return app


def _get_app_args() -> dict:
    args = dict(
        title='Gerador de Times',
        description='@ Gerador de Times API',
        version='1.0.0',
        redoc_url=None
    )
    return args


def _config_app_events(app):
    app.add_event_handler("startup", apply_migrations)
    return app


def _config_app_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
    )
    app.add_middleware(
        ContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin(),
            plugins.ForwardedForPlugin(),
        )
    )
    app.add_middleware(
        DBSessionMiddleware,
        custom_engine=engine,
        commit_on_exit=True
    )
    return app


def _config_app_routers(app):
    routers = get_routers()
    routers.sort(key=lambda r: r.get("prefix"))
    [app.include_router(**r) for r in routers]
    return app


def _config_app_exceptions(app):
    app.add_exception_handler(ApiBaseException, generic_handler)
    return app
