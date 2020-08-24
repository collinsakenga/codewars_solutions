from collections import Counter


def mix(s1, s2):
    result1 = Counter([i for i in s1 if i.islower()])
    result2 = Counter([i for i in s2 if i.islower()])
    final = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        if result1.get(i, 0) > result2.get(i, 1):
            final.append("1:"+i*result1[i])
        elif result2.get(i, 0) > result1.get(i, 1):
            final.append("2:"+i*result2[i])
        elif result1.get(i, 0) == result2.get(i, -1) and result1.get(i, 0) >= 2:
            final.append("=:"+i*result1[i])
    final.sort()
    final.sort(key=len, reverse=True)
    return "/".join(final)


3
