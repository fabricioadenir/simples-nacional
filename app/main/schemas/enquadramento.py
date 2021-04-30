from pydantic import BaseModel
from typing import Optional
from .empresa import Empresa


class Enquadramento(BaseModel):
    dados: Optional[Empresa] = None
    alguma_coisa: str


class ChaveAcesso(BaseModel):
    cnpj: str
    cpf: str
