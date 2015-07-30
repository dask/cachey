import sys


def nbytes(o):
    """ Number of bytes of an object

    >>> nbytes(123)  # doctest: +SKIP
    24

    >>> nbytes('Hello, world!')  # doctest: +SKIP
    50

    >>> import numpy as np
    >>> nbytes(np.ones(1000, dtype='i4'))
    4000
    """
    if hasattr(o, 'nbytes'):
        return o.nbytes
    n = str(type(o))
    if 'pandas' in n and ('DataFrame' in n or 'Series' in n):
        return sum(b.values.nbytes * (10 if b.values.dtype == 'O' else 1)
                   for b in o._data.blocks)  # pragma: no cover
    else:
        return sys.getsizeof(o)
