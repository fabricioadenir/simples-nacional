from .... import config
from loguru import logger
from ...schemas.enquadramento import ChaveAcesso


def enquadrar(dados: ChaveAcesso):
    cnpj = dados.cnpj
    titulo = dados.cpf

    try:
        logger.info("Realizando operação.")
    except:
        logger.error("Erro na operação.")
