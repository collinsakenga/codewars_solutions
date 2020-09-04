def find_children(dancing_brigade):
    return "".join(sorted(dancing_brigade, key=lambda x: (first(x), second(x))))


def first(s):
    return ord(s.lower())


def second(s):
    return 0 if s.isupper() else 1
