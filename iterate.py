"""
Convenience functions for iterators.

"""
import itertools

# from: http://sametmax.com/parcourir-un-iterable-par-morceaux-en-python/
def chunks(iterable, size, output_format=iter):
    """ 
    Return a generator object iterating over iterable in chunks of size
    size.
    This generator will be converted to output_format, which needs to be
    an iterator type.

    Usage:

    >>> l = [15, 78, 19, 88, 666, 12, 42]
    >>> for c in chunks(l, 3, tuple):
    ...     print c
    (15, 78, 19)
    (88, 666, 12)
    (42,)
    >>> s = "Hello World!"
    >>> for c in chunks(s, 4, "-".join):
    ...     print c
    H-e-l-l
    o- -W-o
    r-l-d-!
    """
    it = iter(iterable)
    while True:
        yield output_format(
            itertools.chain(
                (it.next(),),
                itertools.islice(it, size-1)
            )
        )
