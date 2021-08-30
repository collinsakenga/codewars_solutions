def mineLocation(field):
    for i,j in enumerate(field):
        try:
            return [i, j.index(1)]
        except:
            pass