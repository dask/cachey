from cachey import Scorer


def test_Scorer():
    s = Scorer(10)

    a = s.touch('x', 10)
    b = s.touch('y', 1)
    assert a > b

    a = s.touch('x')
    b = s.touch('x')
    assert a < b


def test_limit():
    s = Scorer(10, limit=10)
    a = s.touch('x', 20)
    assert a > 0
    assert 'x' not in s.cost  # don't take up space with bad elements
    assert 'x' not in s.time
