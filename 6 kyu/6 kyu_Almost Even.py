def split_integer(num, parts):
    quotient = num//parts
    remainder = num % parts
    result = []
    for num in range(1, parts+1):
        if num > parts-remainder:
            result.append(quotient+1)
        else:
            result.append(quotient)
    return result
