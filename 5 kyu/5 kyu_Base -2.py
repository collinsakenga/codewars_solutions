def int_to_negabinary(i):
    res = []
    while i != 0:
        quotient, remainder = divmod(i, -2)
        res.append(remainder+2 if remainder < 0 else remainder)
        i = quotient+1 if remainder < 0 else quotient
    return "".join(str(i) for i in res)[::-1] if res else "0"


def negabinary_to_int(s):
    total = 0
    for i, j in enumerate(s[::-1]):
        if j == "0":
            continue
        total += 2**i if i % 2 == 0 else -(2**i)
    return total
