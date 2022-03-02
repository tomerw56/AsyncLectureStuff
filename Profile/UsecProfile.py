import TestClass
import asyncio
import cProfile
import functools
import logging
import pstats
import random
import signal
import string
import uuid
import io

if __name__ == "__main__":
    example=TestClass.TesClass(heavy_second_function=False)
    pr = cProfile.Profile()
    pr.enable()
    example.RunMe()
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s)
    ps.sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats()
    print(s.getvalue())