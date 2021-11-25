import uvicorn
from fastapi import FastAPI

from sentry_client import sentry
from tasks import task_async_function_example, task_sync_function_example

app = FastAPI()


@app.on_event("startup")
def sentry_init():
    print("Connection to Sentry...")
    sentry.senty_init(app)


@app.get("/")
def read_root():
    task_async_function_example.delay()
    task_sync_function_example.delay()
    return {"Hello": "World"}


if __name__ == '__main__':
    # Лог со всеми настройками системы
    uvicorn.run("main:app", host="127.0.0.1", port=7040, log_level="debug")
