def sequence_gen(*args):
    for i in args:
        yield i
    num=sum(args)
    res=[i for i in args]
    length=len(args)
    while True:
        res.append(num)
        num+=res[-1]-res[-length-1]
        yield res[-1]
        
        