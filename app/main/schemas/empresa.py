from pydantic import BaseModel


class ConfigMni(BaseModel):
    url: str
    usuario: str
    senha: str
    usarwsdl: str
    versaomni: str


class Empresa(BaseModel):
    cnpj: str
    cpf: str
    titulo: str
    recibo: str
    ano: str


class ChaveAcesso(BaseModel):
    cnpj: str
    cpf: str
