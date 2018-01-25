import numpy as np

def validate(x, numeric_only=False):
    """
    performs basic checks on input
    """
    if np.isscalar(x):
        raise ValueError("input must be list")

    if numeric_only and not all(isinstance(i, (int, float)) for i in x):
        raise ValueError("for quicksort, all elements must be numeric")

    if any(isinstance(i, list) for i in x):
        print(i)
        raise ValueError("elements may not be lists")

    type1 = type(x[0])
    if not all(isinstance(i, type1) for i in x):
        raise ValueError("elements must be of similar type")


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
    validate(x)
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    #assert is_sorted(x)
    return x

def partition(x, l, h):
    p = l
    for j in range(l + 1, h + 1):
        if x[j] < x[l]:
            p += 1
            x[j], x[p] = x[p], x[j]
    x[p], x[l] = x[l], x[p]
    return p

def qsort(x, low, high):
    if low < high:
        p = partition(x, low, high)
        qsort(x, low, p - 1)
        qsort(x, p + 1, high)

def quicksort(x):
    """
    Describe how you are sorting `x`
    """
    #validate(x, True)
    print(x)
    qsort(x, 0, len(x) -1)
    print(x)
    return x

quicksort(list(range(1,11))[::-1])