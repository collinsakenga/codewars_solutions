def sequence_gen(*args):
    res=[i for i in args]
    for i in res:
        yield i
    while True:
        res.append(sum(res[-len(args):]))
        yield res[-1]