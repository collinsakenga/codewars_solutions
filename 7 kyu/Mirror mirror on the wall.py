def mirror(data: list) -> list:
    res=sorted(data)
    return res[:-1]+res[::-1]
