import numpy as np
from example import algs
import pytest

def num_arrays():
    return [np.random.rand(10), np.random.uniform(-100, 100, 10),   list(range(1,11))[::-1]]

def alph_arrays():
    return['a', 'az', '(j', "A", "{OF#"]

def bad_arrays():
    return[['a', 1], [[1]], [{1, 2, 3}, 4, 5]]


def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    l = num_arrays()

    for x in l:
        algs.bubblesort(x)
        assert all(x[i] <= x[i+1] for i in range(0, len(x) - 1))
    
    m = alph_arrays()
    algs.bubblesort(m)
    assert all(m[i] <= m[i+1] for i in range(0, len(m) - 1))

    b = bad_arrays()
    with pytest.raises(ValueError):
        for i in b:
            algs.quicksort(i)

def test_quicksort():
    l = num_arrays()
    for x in l:
        algs.quicksort(x)
        print(x)
        assert all(x[i] <= x[i+1] for i in range(0, len(x) - 1))

    m = alph_arrays()
    with pytest.raises(ValueError):
        algs.quicksort(m)

    b = bad_arrays()
    with pytest.raises(ValueError):
        for i in b:
            algs.quicksort(i)

