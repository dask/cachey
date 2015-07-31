from .nbytes import nbytes
from .score import Scorer
from heapdict import heapdict
import time

def cost(nbytes, time):
    return float(time) / nbytes / 1e9


def memo_key(args, kwargs):
    result = (args, frozenset(kwargs.items()))
    try:
        hash(result)
    except TypeError:
        result = tuple(map(id, args)), str(kwargs)
    return result


class Cache(object):
    def __init__(self, available_bytes, limit, scorer=None, halflife=1000, nbytes=nbytes, cost=cost):
        if scorer is None:
            scorer = Scorer(halflife)
        self.scorer = scorer
        self.available_bytes = available_bytes
        self.limit = limit
        self.get_nbytes = nbytes
        self.cost = cost

        self.data = dict()
        self.heap = heapdict()
        self.nbytes = dict()
        self.total_bytes = 0

    def put(self, key, value, cost, nbytes=None):
        if nbytes is None:
            nbytes = self.get_nbytes(value)
        if cost < self.limit:
            score = self.scorer.touch(key, cost)
            if not self.heap or score > self.heap.peekitem()[1]:
                self.data[key] = value
                self.heap[key] = score
                self.nbytes[key] = nbytes
                self.total_bytes += nbytes
                self.shrink()
                return score

    def get(self, key, default=None):
        self.scorer.touch(key)
        if key in self.data:
            return self.data[key]
        else:
            return default

    def retire(self, key):
        val = self.data.pop(key)
        self.total_bytes -= self.nbytes.pop(key)

    def shrink(self):
        if self.total_bytes <= self.available_bytes:
            return

        while self.total_bytes > self.available_bytes:
            key, score = self.heap.popitem()
            self.retire(key)

    def memoize(self, func, key=memo_key):
        def cached_func(*args, **kwargs):
            k = (func, key(args, kwargs))

            result = self.get(k)
            if result is None:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()

                nb = nbytes(result)

                self.put(k, result, cost(nb, end - start), nbytes=nb)
            return result
        return cached_func

