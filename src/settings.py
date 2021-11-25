from pydantic import BaseSettings


class Config(BaseSettings):
    CELERY_BROKER_URL: str
    SENTRY_URL: str

    class Config:
        env_file = '.env'


config = Config()
