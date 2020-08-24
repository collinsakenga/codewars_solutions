def test_it(a, b):
    sum_a = 0
    sum_b = 0
    for addDigit in str(a):
        sum_a += int(addDigit)
    for addDigit2 in str(b):
        sum_b += int(addDigit2)
    return sum_a*sum_b
