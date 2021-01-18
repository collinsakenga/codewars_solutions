def diff(poly):
    return [j*(len(poly)-1-i) for i,j in enumerate(poly[:-1])]