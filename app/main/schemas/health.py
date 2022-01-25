from pydantic import BaseModel
# from typing import Optional
from datetime import datetime

from ... import config


class Health(BaseModel):
    name: str = config.PROJECT_NAME
    description: str = config.PROJECT_DESCRIPTION
    version: str = config.PROJECT_VERSION
    timestamp: datetime
    uptime: str
    dependencies: list = []
