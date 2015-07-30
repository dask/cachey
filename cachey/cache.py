from .nbytes import nbytes
from heapdict import heapdict

def cost(nbytes, time):
    return float(time) / nbytes / 1e9

class Cache(object):
    def __init__(self, scorer, available_bytes, limit, nbytes=nbytes, cost=cost):
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
