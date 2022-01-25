from pydantic import BaseModel, Field
from typing import Optional


class CnpjEmpresa(BaseModel):
    cnpj: str = Field(
        title="Número do CNPJ",
        min_length=14,
        max_length=14
    )
    cpf: str = Field(
        title="Número do CPF",
        min_length=11,
        max_length=11
    )


class Retorno(BaseModel):
    dados: Optional[list]
    chave: Optional[str] = Field(
        title="Chave",
        description=("Chave de acesso ao Simples Nacional")
    )
    data_resultado: Optional[str] = Field(
        title="Data",
        description=("Data para consulta do status da solicitação.\n"
                     "Exemplo: ddmmyyyy => 10101999"),
        min_length=10,
        max_length=10
    )
    status: bool = Field(
        title="Status da criação da chave",
        description="Se sucesso retorna True. Caso erro retorna False.",
        default=False
    )
    msg: list = None
    erro_operacao: bool = Field(
        title="Erro de operação",
        description="Se apresentar erro retorna True.",
        default=False
    )
