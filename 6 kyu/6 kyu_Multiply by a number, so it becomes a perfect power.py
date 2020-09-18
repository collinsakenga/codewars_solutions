def mul_power(n, k):
    res = factorization(n)
    total = 1
    for i in set(res):
        if res.count(i) % k == 0:
            continue
        total *= i**(k-(res.count(i)) % k)
    return total


def factorization(n):
    factor = 2
    res = []
    while factor*factor <= n:
        if n % factor == 0:
            n //= factor
            res.append(factor)
            factor = 2
        else:
            factor += 1
    res.append(int(n))
    return res
