import itertools
temp = set()
res = []


def hamming(n):
    global res
    if not temp:
        for combo in itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]*3, 3):
            temp.add(combo)
    if not res:
        res = list(temp)
        for i, j in enumerate(res):
            res[i] = (2**(j[0])*3**(j[1])*5**(j[2]))
        res.sort()
    return res[n-1]