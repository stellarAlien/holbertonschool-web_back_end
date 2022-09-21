#!/usr/bin/env python3
'''
yields values after sleeping
'''

import asyncio
from random import uniform


async def async_generator() -> float:
    '''yield numbers asynchronously'''
    for _ in range(10):
        # https://splunktool.com/why-does-asynciosleep0-make-my-code-faster
        await asyncio.sleep(1)
        yield uniform(0, 10)
