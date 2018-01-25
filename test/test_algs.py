import numpy as np
from example import algs

def num_arrays():
    return [np.random.rand(10), np.random.uniform(-100, 100, 10),   list(range(1,11))[::-1]]



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
    

def test_quicksort():
    l = num_arrays()
    for x in l:
        algs.quicksort(x)
        print(x)
        assert all(x[i] <= x[i+1] for i in range(0, len(x) - 1))

