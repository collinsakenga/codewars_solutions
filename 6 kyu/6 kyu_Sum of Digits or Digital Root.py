def digital_root(n):
    sum_digits = 0
    while True:
        sum_digits += n % 10
        n = n//10
        if n == 0:
            n = sum_digits
            sum_digits = 0
            if n < 10:
                break
    return n
