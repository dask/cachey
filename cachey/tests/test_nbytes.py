from cachey import nbytes


def test_obj():
    assert nbytes('hello'*100) > 500


try:
    import pandas as pd
    import numpy as np
    def test_pandas():
        x = np.random.random(1000)
        i = np.random.random(1000)
        s = pd.Series(x, index=i)
        assert nbytes(s) == nbytes(x) + nbytes(i)

        df = pd.DataFrame(s)
        assert nbytes(df) == nbytes(s)

except ImportError:
    pass
