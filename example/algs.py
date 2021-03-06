import numpy as np

#global variables used for counting quicksort
qcond = 0
qasgn = 0 


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
    if type1 == int or type1 == float:
        if not all(isinstance(i, (int, float)) for i in x):
            raise ValueError("elements must be of similar type")

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    For an array of n elements:
        pass through the array n times
        on each pass, swap adjacent values that are out of order
    returns tuple of sorted array, # conditionals, # assignments
    """
    cond = 0
    asgn = 0

    if len(x) == 0:
        return x

    validate(x)
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            cond += 1
            if x[j] > x[j+1]:
                asgn += 2
                x[j], x[j+1] = x[j+1], x[j]
    return (x, cond, asgn)

def partition(x, l, h):
    """
    finds a pivot point
    reorders list by comparing each element to the pivot
    """
    global qasgn
    qasgn += 1
    p = l
    for j in range(l + 1, h + 1):
        if x[j] < x[l]:
            qasgn += 3
            p += 1
            x[j], x[p] = x[p], x[j]
    qasgn += 2
    x[p], x[l] = x[l], x[p]
    return p

def qsort(x, low, high):
    """
    calls partition function to break list into two parts
    recursively calls itself to sort each part
    """
    global qcond
    qcond += 1
    if low < high:
        qcond += high - low
        p = partition(x, low, high)
        qsort(x, low, p - 1)
        qsort(x, p + 1, high)

def quicksort(x):
    """
    calls qsort to perform quicksort algorithm
    quicksort cannot handle strings, all elements must be numeric
    uses global variables to count conditionals, assignments
    returns tuple of sorted list, # conditionals, # assignments
    """
    global qcond
    qcond = 0

    global qasgn
    qasgn = 0

    if len(x) == 0:
        return x
    validate(x, True)

    qsort(x, 0, len(x) -1)
    return (x, qcond, qasgn)
