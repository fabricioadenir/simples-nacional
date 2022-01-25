from pydantic import BaseModel, Field
from typing import Optional
from app.main.schemas.base import CnpjEmpresa


class SolicitarEnquadramento(CnpjEmpresa):
    chave: str = Field(
        title="Chave de Acesso",
        min_length=12,
        max_length=12
    )
    data_cnpj: str = Field(
        title="Data",
        description=(
            "Data do ultimo deferimento de inscrição (Estadual ou Municipal)"),
        min_length=8,
        max_length=8
    )


class RetornarEnquadramento(BaseModel):
    dados: SolicitarEnquadramento = Field(
        title="Dados da Requisição"
    )
    status: bool = Field(
        title="Status do Enquadramento",
        description="Se sucesso retorna True. Caso erro retorna False.",
        default=False
    )
    data_resultado: Optional[str] = Field(
        title="Data",
        description=("Data para consulta do status da solicitação.\n"
                     "Exemplo: ddmmyyyy => 10101999"),
        min_length=10,
        max_length=10
    )
    msg: Optional[str] = Field(
        title="Mensagem da Operação",
        description="Será retornado somente em caso de erro."
    )
    erro_operacao: bool = Field(
        title="Erro de operação",
        description="Se apresentar erro retorna True.",
        default=False
    )
