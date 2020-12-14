from typing import Generator, TypeVar, List
from itertools import tee
from types import GeneratorType

T = TypeVar("T")
async def anext(async_generator: Generator[T, None, None], default_value: T=None):
    try:
        return await async_generator.__anext__()
    except StopAsyncIteration:
        return default_value

# Memoization decorator (caches results), works with generators too.
Tee = tee([], 1)[0].__class__
def memoized(f):
    cache={}
    def ret(*args):
        if args not in cache:
            cache[args]=f(*args)
        if isinstance(cache[args], (GeneratorType, Tee)):
            cache[args], r = tee(cache[args])
            return r
        return cache[args]
    return ret

def __make_hashable(*args):
    for arg in args:
        if isinstance(arg, List):
            yield tuple(arg)
        else:
            yield arg