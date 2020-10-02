from collections import Counter


def anagram_difference(w1, w2):
    if not w1:
        return len(w2)
    elif not w2:
        return len(w1)
    temp1 = Counter(w1)
    temp2 = Counter(w2)
    return sum(j for j in (temp2-temp1).values())+sum(j for j in (temp1-temp2).values())
