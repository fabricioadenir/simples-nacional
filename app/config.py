import decouple

# Config
TIMEZONE = decouple.config("TIMEZONE", default="America/Sao_Paulo")

# Project
PROJECT_VERSION = '0.1.0'
PROJECT_NAME = 'SimplesNacional'
PROJECT_DESCRIPTION = 'API de serviço do Portal do Simples Nacional.'

APP_ENV = decouple.config("APP_ENV", default="dev")

# LOG Config
LOG_LEVEL = decouple.config("LOG_LEVEL", default="INFO")

# Tenant config
TENANT_NAME = decouple.config("TENANT_NAME", default="")

# Simples Nacional
SIMPLES_URL = decouple.config(
    "SIMPLES_URL", default="http://www8.receita.fazenda.gov.br/simplesnacional/")
