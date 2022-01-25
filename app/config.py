import decouple
from pathlib import Path
import os

ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
ROOT1 = ROOT.as_posix()
# Config
TIMEOUT = decouple.config("TIMEOUT", default=60)
TIMEZONE = decouple.config("TIMEZONE", default="America/Sao_Paulo")
TYPE_BROWSER = decouple.config("TYPE_BROWSER", default="firefox")
EXECUTABLE_PATH = decouple.config(
    "EXECUTABLE_PATH", default=f"{ROOT}/webdriver/geckodriver.exe")
CONTAINER_SELENIUM = decouple.config(
    "CONTAINER_SELENIUM", default="http://127.0.0.1:4444/wd/hub")

DOCKER_EXECUTION = decouple.config("DOCKER_EXECUTION", cast=bool, default=0)

# Death by Captcha https://deathbycaptcha.com/api
CAPTCHA_USER = decouple.config("CAPTCHA_USER", default="")
CAPTCHA_PASS = decouple.config("CAPTCHA_PASS", default="")
CAPTCHA_TOKEN = decouple.config(
    "CAPTCHA_TOKEN",
    default=(""))

# Anti Captcha https://anti-captcha.com/pt
ANTI_CPT_TOKEN = decouple.config(
    "ANTI_CPT_TOKEN", default="")

# Project
PROJECT_VERSION = '0.1.0'
PROJECT_NAME = 'SimplesNacional'
PROJECT_DESCRIPTION = 'API de serviço do Portal do Simples Nacional.'

APP_ENV = decouple.config("APP_ENV", default="dev")

# LOG Config
LOG_LEVEL = decouple.config("LOG_LEVEL", default="INFO")

# Simples Nacional
SIMPLES_URL = decouple.config(
    "SIMPLES_URL", default="http://www8.receita.fazenda.gov.br/simplesnacional/")
