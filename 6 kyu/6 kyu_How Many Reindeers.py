def reindeer(presents):
    if presents > 180:
        raise Exception()
    return 3+(presents-1)//30
