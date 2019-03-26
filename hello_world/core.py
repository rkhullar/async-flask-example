from typing import NamedTuple, List
import asyncio
import logging


class HelloWorldParams(NamedTuple):
    app_env: str = 'sbx'


class HelloWorld:

    def __init__(self, params: HelloWorldParams = None, **kwargs):
        self.params = params or HelloWorldParams(**kwargs)

    @staticmethod
    async def hello(message: str = 'hello world', count: int = 1, delay: int = 1) -> List[str]:
        await asyncio.sleep(delay)
        return [message for _ in range(count)]
