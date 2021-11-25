import asyncio

from celery import Celery

from settings import config
from utils import async_function_example, sync_function_example

celery = Celery(broker=config.CELERY_BROKER_URL)


def run_async_task(func, *args, **kwargs):
    """
    Запуск таска через event-loop.

    Решение взято из статьи https://habr.com/ru/post/502380/
    """
    asyncio.run(func(*args, **kwargs))


@celery.task
def task_async_function_example(*args, **kwargs):
    run_async_task(async_function_example, *args, **kwargs)


@celery.task
def task_sync_function_example(*args, **kwargs):
    sync_function_example(*args, **kwargs)
