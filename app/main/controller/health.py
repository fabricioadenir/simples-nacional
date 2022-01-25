from fastapi import APIRouter
from datetime import datetime
from ... import config

from ..schemas.health import Health
import requests
from http import HTTPStatus
from loguru import logger

from dateutil.zoneinfo import get_zonefile_instance

router = APIRouter()


@router.get("/health", response_model=Health)
async def health():
    """Disponibiliza a saúde da API

    Returns:
        health: Retorna um Json com informações importantes da API.
    """
    logger.info("HealthCheck da API.")

    def _get_up_time(start_time):
        default_zone = get_zonefile_instance()
        date_now = datetime.now()
        delta_str = str(date_now - start_time)
        time_zone = default_zone.get(config.TIMEZONE, 'UTC')
        start_time_str = start_time.astimezone(time_zone).isoformat()
        return f"{delta_str} from {start_time_str}"

    def check_dependencies(url):
        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK:
                return True
            else:
                return False
        except Exception:
            return False

    health = Health(
        timestamp=datetime.now(),
        uptime=_get_up_time(config.START_TIME)
    )

    health.dependencies.append(
        {"name": "SimplesNacional",
         "status": check_dependencies(config.SIMPLES_URL)}
    )
    return health
