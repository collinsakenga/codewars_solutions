from itertools import combinations


def choose_best_sum(t, k, ls):
    combo = combinations(ls, k)
    comp = 0
    for i in combo:
        max = sum(i)
        if max > comp and max < t:
            comp = max
        elif max == t:
            return max
    return comp if comp != 0 else None
