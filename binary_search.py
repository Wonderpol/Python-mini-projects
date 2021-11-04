# Implementation of binary search al and a proof that naive search is slower

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

