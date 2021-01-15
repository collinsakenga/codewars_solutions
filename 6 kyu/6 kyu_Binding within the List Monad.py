def bind(lst,func):
    return sum([func(i) for i in lst], [])