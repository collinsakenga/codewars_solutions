from itertools import combinations
def closest_sum(ints, num):
    return sorted([sum(i) for i in combinations(ints, 3)], key=lambda x: abs(x-num))[0]