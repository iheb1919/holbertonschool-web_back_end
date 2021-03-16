#!/usr/bin/env python3
"""
Measure the runtime
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """
    function with integers n and max_delay as arguments that measures
    the total execution time for wait_n(n, max_delay)
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
