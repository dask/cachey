from cachey import Cache, Scorer, nbytes

def test_cache():
    s = Scorer(halflife=10)
    c = Cache(s, available_bytes=nbytes(1) * 3, limit=100)

    c.put('x', 1, 10)
    assert c.get('x') == 1

    c.put('a', 1, 10)
    c.put('b', 1, 10)
    c.put('c', 1, 10)
    assert set(c.data) == set('abc')
    c.put('d', 1, 10)
    assert set(c.data) == set('bcd')
