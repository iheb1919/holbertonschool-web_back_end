#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """ asynchronous coroutine that returns arandom value
    """
    randomValue = random.uniform(0, max_delay)
    await asyncio.sleep(randomValue)
    return randomValue
