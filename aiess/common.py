from typing import Generator, TypeVar

T = TypeVar("T")
async def anext(async_generator: Generator[T, None, None], default_value: T=None):
    try:
        return await async_generator.__anext__()
    except StopAsyncIteration:
        return default_value