def prime_bef_aft(num):
    change = 1
    res = [None, None]
    while None in res:
        if not res[0] and is_prime(num-change):
            res[0] = num-change
        if not res[1] and is_prime(num+change):
            res[1] = num+change
        change += 1
    return res
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True