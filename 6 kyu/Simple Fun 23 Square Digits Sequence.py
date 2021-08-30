def square_digits_sequence(n):
    res=[n]
    while len(set(res))==len(res):
        res.append(square_sum(res[-1]))
    return len(res)
def square_sum(n):
    total=0
    for i in str(n):
        total+=int(i)**2
    return total