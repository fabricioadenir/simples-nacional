from fastapi import APIRouter
from ..schemas.chave_acesso import CriaChave, RetornaChave
from ..schemas.enquadramento import SolicitarEnquadramento, RetornarEnquadramento
from ..services.menu_opcao.enquadrar import enquadrar
from ..services.menu_opcao.criar_chave import criar_chave
from loguru import logger

router = APIRouter()


@router.post("/criar-chave-acesso", response_model=RetornaChave)
async def criar_chave_acesso(payload: CriaChave):
    """Responsabilidade de criação de uma nova chave de acesso.

    Args:
        payload (CriaChave): recebe um json no padrão informado na
         documentação: http://localhost:8000/redoc#tag/Opcoes

    Returns:
        resultado: Retorna um json no formato do contrato.
    """
    cnpj = payload.cnpj
    logger.info(f"Solicitado criação de chave de acesso. CNPJ: {cnpj}")
    resultado = criar_chave(payload)
    return resultado


@router.post("/enquadrar", response_model=RetornarEnquadramento)
async def enquadrar_simples_nacional(payload: SolicitarEnquadramento):
    """Responsabilidade de solicitar o enquadramento no simples nacional

    Args:
        payload (SolicitarEnquadramento): recebe um json no padrão informado na
         documentação: http://localhost:8000/redoc#tag/Opcoes

    Returns:
        resultado: Retorna um json no formato do contrado.
    """
    cnpj = payload.cnpj
    logger.info(f"Solicitado enquadramento ao Simples Nacional. CNPJ: {cnpj}")

    resultado = enquadrar(payload)
    return resultado
