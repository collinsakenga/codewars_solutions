def combine(*args):
    return [j[index] for index in range(max(len(item) for item in args)) for j in args if index<len(j)]