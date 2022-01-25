from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.main.controller import health, opcao

from datetime import datetime
from . import config
from app.main.schemas.base import Retorno


def create_app(config_name):
    app = FastAPI(
        title=config.PROJECT_NAME,
        description=config.PROJECT_DESCRIPTION,
        version=config.PROJECT_VERSION,
    )

    app.include_router(health.router, tags=["Health"])
    app.include_router(
        opcao.router, prefix="/api/simples-nc/opcoes", tags=["Menu Opções"])

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        erros = []
        erros_ = exc.errors()
        print(f"Erro: {erros_}")
        for erro in erros_:
            erros.append({
                "campo": erro.get("loc")[1],
                "msg": erro.get("msg"),
                "tipo": erro.get("ctx")
            }
            )

        retorno = Retorno(
            msg=erros,

        )
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(retorno),
        )
    config.START_TIME = datetime.now()

    return app
