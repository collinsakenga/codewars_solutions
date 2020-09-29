from collections import Counter


def points(dice):
    if len(set(dice)) == 1:
        return 50
    check = Counter(dice)
    for i, j in check.items():
        if j == 4:
            return 40
        elif j == 3:
            return 0 if len(check) == 3 else 30
    for i in [12345, 23456, 34561, 13654, 62534]:
        if Counter(str(i)) == check:
            return 20
    return 0
