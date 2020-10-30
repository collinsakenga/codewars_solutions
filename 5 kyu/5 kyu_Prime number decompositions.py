from collections import Counter
def getAllPrimeFactors(n):
    if not isinstance(n, int) or n <= 0:
        return []
    factor = 2
    res = []
    while factor*factor <= n:
        if n % factor == 0:
            res.append(factor)
            n //= factor
            factor = 2
        else:
            factor += 1
    res.append(n)
    return res


def getUniquePrimeFactorsWithCount(n):
    if not isinstance(n, int) or n <= 0:
        return [[], []]
    res = Counter(getAllPrimeFactors(n))
    return [[j for j in res.keys()], [j for j in res.values()]]


def getUniquePrimeFactorsWithProducts(n):
    if not isinstance(n, int) or n <= 0:
        return []
    res = Counter(getAllPrimeFactors(n))
    return [i**j for i, j in res.items()]