from pydantic import BaseModel, Field
from typing import Optional
from .base import CnpjEmpresa


class CriaChave(CnpjEmpresa):
    titulo_eleitoral: Optional[list] = Field(
        title="Número do Titulo de eleitor",
        description="Lista de valores possiveis para titulo."
    )
    data_nascimento: Optional[str] = Field(
        title="Data de nascimento",
        description="Exemplo: ddmmyyy => 10101999",
        min_length=8,
        max_length=8
    )
    recibo_irpf: Optional[list] = Field(
        title="Número do Recibo do IRPF",
        description="Lista com recibos válidos."
    )
    data_recibo: Optional[str] = Field(
        title="Data do Recibo IRPF",
        min_length=4,
        max_length=4
    )


class RetornaChave(BaseModel):
    dados: CriaChave = Field(
        title="Dados da Requisição"
    )
    status: bool = Field(
        title="Status da criação da chave",
        description="Se sucesso retorna True. Caso erro retorna False.",
        default=False
    )
    chave: Optional[str] = Field(
        title="Chave",
        description=("Chave de acesso ao Simples Nacional")
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
