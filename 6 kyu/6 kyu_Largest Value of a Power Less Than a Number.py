from math import gcd


def largest_power(n):
    if n == 1:
        return (0, -1)
    elif n < 5:
        return (1, -1)
    temp = n-1
    while temp > 0:
        res = factorization(temp)
        if len(res) != 1:
            if len(set(res)) == 1:
                next = gen_factors(len(res))
                return (temp, len(next))
            else:
                solution = []
                flag = True
                for i in set(res):
                    if res.count(i) < 2:
                        flag = False
                        break
                    solution.append(res.count(i))
                if flag:
                    for i in range(1, len(solution)):
                        if i != 1:
                            check = gcd(check, solution[i])
                        else:
                            check = gcd(solution[i], solution[i-1])
                    if check > 1:
                        for i in solution:
                            if i % check != 0:
                                flag = False
                                break
                        if flag:
                            next = gen_factors(check)
                            return (temp, len(next))
        temp -= 1


def factorization(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    if n == 1:
        return res
    factor = 3
    while factor*factor <= n:
        if n % factor == 0:
            n //= factor
            res.append(factor)
            factor = 3
        else:
            factor += 1
    res.append(n)
    return res


def gen_factors(n):
    res = [n]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i != n//i:
                res.append(n//i)
    return res
