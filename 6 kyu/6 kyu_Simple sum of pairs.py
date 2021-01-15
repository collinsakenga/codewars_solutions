def solve(n):
    if n <= 10:
        return n
    max = int((len(str(n))-1)*"9")
    return len(str(max))*9+digit_sum(n-max)


def digit_sum(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total