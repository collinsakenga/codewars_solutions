def sum_of_multiples(number: int, lst: list) -> int:
    res=set()
    for n in lst:
        res|={i for i in range(n, number, n)}
    return sum(res)