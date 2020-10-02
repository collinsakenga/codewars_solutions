res = [0, 1]
for i in range(3, 5001):
    res.append((i-1)*(res[-1]+res[-2]))


def all_permuted(array_length):
    return res[array_length-1]
