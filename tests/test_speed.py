import sys
import pytest
import asyncio
import random
import time
import numpy as np
sys.path.insert(1, '../key-value');
import keyvalue

#build a store of values of max recommeneded size
def build_database():
    database = keyvalue.KeyValue()
    loop = asyncio.get_event_loop()
    total = 0
    times = []
    for x in range(keyvalue.MAX_SIZE):
        loop.run_until_complete(database.put(f"key{x}",f"value{x}"))
    randomlist = [];
    for i in range(500):
        n = random.randint(1,MAX_SUSTAINABLE_VALUES)
        randomlist.append(n)
    for n in randomlist:
        t0 = time.perf_counter()
        loop.run_until_complete(database.retrieve(f"key{n}"))
        t1 = time.perf_counter()
        t = t1-t0
        total += t
        times.append(t)
    return times;
#test ninety fifth percentile time less then 1 millisecond
def test_ninety_fifth():
    times = build_database()
    assert np.percentile(times,99) < 0.001
#test ninety nine percentile time less then 5 millisecond
def test_ninety_nine():
    times = build_database()
    assert np.percentile(times,99) < 0.005


