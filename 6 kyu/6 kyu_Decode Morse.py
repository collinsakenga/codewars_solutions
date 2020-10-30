def decode(s):
    TOME['']=' '
    return "".join(TOME[i] for i in s.split(" ")) if s else ""