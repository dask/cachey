from collections import defaultdict
from math import log

class Scorer(object):
    """ Object to track scores of cache

    Prefers computations that have the following properties:

    1.  Costly to compute (seconds)
    2.  Cheap to store (bytes)
    3.  Frequently used
    4.  Recently used

    This object tracks both stated costs of keys and a separate score related
    to how frequently/recently they have been accessed.  It uses these to to
    provide a score for the key used by the ``Cache`` object, which is the main
    usable object.

    Example
    -------

    >>> s = Scorer(halflife=10)
    >>> s.touch('x', cost=2)  # score is similar to cost
    2
    >>> s.touch('x')  # scores increase on every touch
    4.138629436111989
    """
    def __init__(self, halflife):
        self.cost = dict()
        self.time = defaultdict(lambda: 0)

        self._base_multiplier = 1 + log(2) / float(halflife)
        self.tick = 1
        self._base = 1

    def touch(self, key, cost=None):
        """ Update score for key

        Provide a cost the first time and optionally thereafter.
        """
        time = self._base

        if cost is not None:
            self.cost[key] = cost
            self.time[key] += self._base
            time = self.time[key]
        else:
            try:
                cost = self.cost[key]
                self.time[key] += self._base
                time = self.time[key]
            except KeyError:
                return

        self._base *= self._base_multiplier
        return cost * time
