#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """
    wait_n should return the list of all the delays (float values)
    """
    list_wait=[]
    for i in range(n):
        list_wait.append(await wait_random(max_delay))
    return sorted(list_wait)
