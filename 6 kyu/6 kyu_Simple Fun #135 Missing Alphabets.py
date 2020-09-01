from collections import Counter


def missing_alphabets(s):
    res = Counter("".join(sorted(s)))
    check = res.most_common(1)[0][1]
    solution = ""
    for i in "abcdefghijklmnopqrstuvwxyz":
        solution += i*(check-res.get(i, 0))
    return solution
