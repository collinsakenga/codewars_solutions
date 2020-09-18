def is_happy(n):
    res = []
    temp = n
    while True:
        if temp == 1:
            return True
        elif temp in res:
            return False
        res.append(temp)
        temp = digit_sum(temp)


def digit_sum(n):
    total = 0
    for i in str(n):
        total += int(i)**2
    return total
