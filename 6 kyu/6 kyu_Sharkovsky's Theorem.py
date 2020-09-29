def sharkovsky(a, b):
    if a == 1:
        return False
    elif b == 1:
        return True
    temp1 = factor(a)
    temp2 = factor(b)
    if temp1.count(2) < temp2.count(2):
        if temp1[0] % 2 == 0 and temp2[0] % 2 == 0 and len(set(temp1)) == len(set(temp2)) == 1:
            return False
        return True
    elif temp1.count(2) == temp2.count(2):
        return True if b > a else False
    if a > b and (temp1[0] == temp1[-1] == temp2[0] == temp2[-1] == 2):
        return True
    return False


def factor(n):
    res = []
    factor = 2
    while factor*factor <= n:
        if n % factor == 0:
            res.append(factor)
            n //= factor
            factor = 2
        else:
            factor += 1
    res.append(n)
    return res
