import itertools


def permutations(string):
    return list(set(["".join(list(i)) for i in itertools.permutations(list(string))]))
