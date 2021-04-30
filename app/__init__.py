from fastapi import FastAPI
from app.main.controller import health, opcao

from datetime import datetime
from . import config


def create_app(config_name):
    app = FastAPI(
        title=config.PROJECT_NAME,
        description=config.PROJECT_DESCRIPTION,
        version=config.PROJECT_VERSION,
    )

    app.include_router(health.router, tags=["Health"])
    app.include_router(
        opcao.router, prefix="/api/simples-nc/opcoes", tags=["Opções"])

    config.START_TIME = datetime.now()

    return app
