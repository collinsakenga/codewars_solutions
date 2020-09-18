def f(n):
    max_even = len(str(n))-1
    if str(n)[0] == "1":
        max_even -= 1
    for i in range(n-1, -1, -1):
        if i % 2 == 0 or i % 3 == 0:
            continue
        if count_even(i) < max_even:
            continue
        if isPrime(i):
            return i


def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def count_even(n):
    count = 0
    for i in str(n):
        if int(i) % 2 == 0:
            count += 1
    return count
