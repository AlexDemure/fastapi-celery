import asyncio
import time


async def async_function_example(time_sleep: int = 5):
    print("Async sleep")
    await asyncio.sleep(time_sleep)
    print("Async sleep end")


def sync_function_example(range_count: int = 5, time_sleep: int = 1):
    for i in range(range_count):
        time.sleep(time_sleep)
        print(i)
