from cachey import Scorer


def test_Scorer():
    s = Scorer(10)

    a = s.touch('x', 10)
    b = s.touch('y', 1)
    assert a > b

    a = s.touch('x')
    b = s.touch('x')
    assert a < b


def test_halflife():
    s = Scorer(1)
    a = s.touch('x', 10)
    b = s.touch('y', 1)
    b = s.touch('y', 1)
    b = s.touch('y', 1)
    b = s.touch('y', 1)
    assert b > a
