import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from settings import config


class SentrySDK:

    @staticmethod
    def senty_init(app):
        """Инициализация сервиса sentry."""

        sentry_sdk.init(
            dsn=config.SENTRY_URL,
            # Sample rate - частота отправки ошибок в %. Максимальное значение 1.0.
            # Если одна и таже ошибка будет повторяться, тогда sentry будет отправлять только каждую четвертую ошибку.
            # Документацией рекомендуется начинать с значения 0.25 и увеличивать при необходимости.
            sample_rate=0.25,
        )
        SentryAsgiMiddleware(app=app)


sentry = SentrySDK()
