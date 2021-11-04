# Implementation of binary search and naive search and compare times of searching
import random
import time


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


if __name__ == '__main__':
    list_len = 5000
    sorted_list = set()
    while len(sorted_list) < list_len:
        sorted_list.add(random.randint(-2*list_len, 2*list_len))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time is equal to: ", (end - start)/list_len, " seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time is equal to: ", (end - start)/list_len, " seconds")