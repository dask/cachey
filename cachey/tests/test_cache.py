from cachey import Cache, Scorer, nbytes
from time import sleep

def test_cache():
    c = Cache(available_bytes=nbytes(1) * 3)

    c.put('x', 1, 10)
    assert c.get('x') == 1

    c.put('a', 1, 10)
    c.put('b', 1, 10)
    c.put('c', 1, 10)
    assert set(c.data) == set('abc')
    c.put('d', 1, 10)
    assert set(c.data) == set('bcd')


def test_memoize():
    c = Cache(available_bytes=nbytes(1) * 3)

    flag = [0]
    def slow_inc(x):
        flag[0] += 1
        sleep(0.01)
        return x + 1

    memo_inc = c.memoize(slow_inc)

    assert memo_inc(1) == 2
    assert memo_inc(1) == 2

    assert list(c.data.values()) == [2]


def test_callbacks():
    hit_flag = [False]
    def hit(key, value):
        hit_flag[0] = (key, value)

    miss_flag = [False]
    def miss(key):
        miss_flag[0] = key

    c = Cache(100, hit=hit, miss=miss)

    c.get('x')
    assert miss_flag[0] == 'x'
    assert hit_flag[0] == False

    c.put('y', 1, 1)
    c.get('y')
    assert hit_flag[0] == ('y', 1)
