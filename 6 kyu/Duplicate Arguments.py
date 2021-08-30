def solution(*args):
    for i in list(set(args)):
        if args.count(i)>1:
            return True
    return False