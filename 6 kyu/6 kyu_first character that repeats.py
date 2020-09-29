from collections import Counter


def first_dup(s):
    dict = {k: v for k, v in Counter(s).items() if v >= 2}
    return sorted(dict.items(), key=lambda x: s.index(x[0]))[0][0] if dict else None
