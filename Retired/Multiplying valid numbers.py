def multy(x=None, y=None):
    if any(not (isinstance(i, int) or isinstance(i, float) or isinstance(i, bool)) for i in (x, y)):
        return False
    return x*y