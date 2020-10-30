import itertools
def flatten(*args):
    args = list(args)
    while True:
        flag = True
        for i, j in enumerate(args):
            if not isinstance(j, list):
                args[i] = [j]
            else:
                flag = False
        if flag:
            return list(itertools.chain.from_iterable(args))
        args = list(itertools.chain.from_iterable(args))