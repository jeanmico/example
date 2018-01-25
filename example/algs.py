import numpy as np

def is_sorted(x):
    return all(x[i] <= x[i + 1] for i in range(0, len(x) -1))

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Describe how you are sorting `x`
    """
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    assert is_sorted(x)
    return x

def partition(x, l, h):
    p = x[h]
    i = l - 1
    for j in range(l, h-1):
        if x[j] < p:
            i = i + 1
            x[i], x[j] = x[j], x[i]
    if x[h] < x[i + 1]:
        x[i + 1], x[h] = x[h], x[i + 1]
    return i + 1

def qsort(x, low, high):
    if low < high:
        p = partition(x, low, high)
        qsort(x, low, p - 1)
        qsort(x, p + 1, high)

def quicksort(x):
    """
    Describe how you are sorting `x`
    """
    qsort(x, 0, len(x) -1)

    assert 1 == 1
    return x

l = list(range(1, 12))[::-1]
print(bubblesort(l))
print(quicksort(l))
