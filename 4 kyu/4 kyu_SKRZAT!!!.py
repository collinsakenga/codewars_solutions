def skrzat(base, number):
    return bin_to_int(number) if base == "b" else int_to_bin(number)


def bin_to_int(s):
    total = 0
    for i, j in enumerate(s[::-1]):
        if j == "0":
            continue
        total += 2**i if i % 2 == 0 else -(2**i)
    return f"From binary: {s} is {total}"


def int_to_bin(n):
    res = []
    value = n
    while n != 0:
        quotient, remainder = divmod(n, -2)
        res.append(remainder+2 if remainder < 0 else remainder)
        n = quotient+1 if remainder < 0 else quotient
    solution = "0" if not res else "".join(str(i) for i in res)[::-1]
    return f"From decimal: {value} is {solution}"
