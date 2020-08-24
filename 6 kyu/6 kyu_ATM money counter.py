def atm(value):
    num = ""
    dollar = ""
    for i in value:
        try:
            test = int(i)
            num += i
        except:
            if i.isalpha():
                dollar += i
            continue
    dollar = dollar.upper()
    num = int(num)
    result = ""
    if dollar not in VALUES:
        return f"Sorry, have no {dollar}."
    if num % VALUES[dollar][0] != 0:
        return f"Can\'t do {num} {dollar}. Value must be divisible by {VALUES[dollar][0]}!"
    compare = VALUES[dollar].copy()
    compare.reverse()
    for i in compare:
        if num//i > 0:
            result += f"{num//i} * {i} {dollar}, "
            num -= num//i*i
    return result[:-2]
