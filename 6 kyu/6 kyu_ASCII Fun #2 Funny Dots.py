def dot(n, m):
    first = ["+"]*(n+1)
    second = ["|"]*(n+1)
    res = ["---".join(first)]
    for i in range(m):
        res.append(" o ".join(second))
        res.append("---".join(first))
    return "\n".join(res)
