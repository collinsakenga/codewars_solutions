from itertools import groupby
def letter_counts(input):
    return [(i, len(list(j))) for i,j in groupby("".join(input.split()))]
