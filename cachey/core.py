from collections import defaultdict
from math import log

class Scorer(object):
    def __init__(self, halflife, limit=None):
        self.cost = dict()
        self.time = defaultdict(lambda: 0)
        self.limit = limit

        self.halflife = halflife
        self._base_multiplier = (1 + log(2)) / 1000.
        self.tick = 1
        self._base = 1

    def touch(self, key, cost=None):
        self.time[key] += self._base
        self._base *= self._base_multiplier

        if cost is not None:
            if self.limit is None or cost < self.limit:
                self.cost[key] = cost
        else:
            try:
                cost = self.cost[key]
            except KeyError:
                return

        return cost * self.time[key]
