from collections import Counter


def solve(arr):
    count = Counter(arr)
    arr = sorted(arr,  key=lambda x: (-count[x], [x]))
    return arr
