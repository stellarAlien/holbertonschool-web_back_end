#!/usr/bin/env python3
'''use task_wairèrandom
'''

from typing import List

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    '''execute max_delay n times'''
    tasks = [asyncio.create_task(wait_random(max_delay)) for x in range(n)]
    res = await asyncio.gather(*tasks)
    return res
