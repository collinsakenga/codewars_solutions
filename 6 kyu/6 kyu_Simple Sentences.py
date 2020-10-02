def make_sentences(parts):
    res = " ".join(parts)
    res = res.replace(" , ", ", ").replace(" .", ".")
    while ".." in res or ",," in res:
        res = res.replace(",,", ",").replace("..", ".")
    return res if res[-1] == "." else res+"."
