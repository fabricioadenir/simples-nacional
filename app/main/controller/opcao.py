from fastapi import APIRouter
from ..schemas.enquadramento import Enquadramento, ChaveAcesso
from ..services.opcao.enquadrar import enquadrar
from loguru import logger

router = APIRouter()


@router.post("/criar-chave-acesso")
async def criar_chave_acesso(payload: ChaveAcesso):
    cnpj = payload.cnpj
    cpf = payload.cpf
    logger.info(f"Solicitado criação de chave de acesso. CNPJ: {cnpj}")
    results = {
        "status": "OK",
        "response": payload
    }
    if cnpj and cpf:
        enquadrar(payload)
    else:
        logger.info("Não informado o 'CNPJ' ou 'CPF' para exclusão.")
    return results


@router.post("/enquadrar")
async def enquadrar_simples_nacional(payload: ChaveAcesso):
    cnpj = payload.cnpj
    cpf = payload.cpf
    logger.info(f"Solicitado enquadramento ao Simples Nacional. CNPJ: {cnpj}")
    results = {
        "remocao": "OK",
        "response": payload
    }
    if cnpj and cpf:
        enquadrar(payload)
    else:
        logger.info("Não informado o 'CNPJ' ou 'CPF' para exclusão.")
    return results
