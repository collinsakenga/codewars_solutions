from itertools import permutations
def kPermutationsOfN(indices,m):
    return [[]] if not (indices and m) else [list(i) for i in permutations(indices, m)]