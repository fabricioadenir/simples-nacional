from app.config import APP_ENV
from app import create_app

app = create_app(APP_ENV)
