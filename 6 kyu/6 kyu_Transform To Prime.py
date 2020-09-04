def minimum_number(numbers):
    if numbers == 0:
        return 1
    total = sum(numbers)
    count = 0
    while True:
        if is_prime(total+count):
            return count
        count += 1


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
