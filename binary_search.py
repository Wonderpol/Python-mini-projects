# Implementation of binary search al and a proof that naive search is slower

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint - 1)
    else:
        # target > list[midpoint]
        return binary_search(list, target, midpoint + 1, high)

