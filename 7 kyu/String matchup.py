from collections import Counter
def solve(a,b):
    counts=Counter(a)
    return [counts.get(i, 0) for i in b]