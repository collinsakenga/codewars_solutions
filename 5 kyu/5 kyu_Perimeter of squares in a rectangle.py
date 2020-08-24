def perimeter(n):
    zero = 1
    one = 1
    if n == 0:
        return zero*4
    elif n == 1:
        return (zero+one)*4
    else:
        total = 2
        for num in range(1, n):
            result = zero+one
            zero = one
            one = result
            total += result
        return total*4
