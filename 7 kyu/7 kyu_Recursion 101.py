def solve(a, b):
    if a == 0 or b == 0:
        return [a, b]
    elif a >= b*2:
        return solve(a-2*b, b)
    elif b >= a*2:
        return solve(a, b-2*a)
    else:
        return [a, b]
