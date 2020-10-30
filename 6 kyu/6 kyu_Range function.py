def range_function(start=0, end=0, step=0):
    return [i+1 for i in range(start)] if not (end or step) else [i for i in range(start, end+1)] if not step else [i for i in range(start, step+1, end)]

