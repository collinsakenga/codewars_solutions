def sum_digits(n):
    while n>=10:
        n=digit_sum(n)
    return n
def digit_sum(n):
    return sum(int(i) for i in str(n))