def digitsum(num):
    total = 0
    for i in range(0, len(num)):
        total += int(num[i])
    return total


def order_weight(strng):
    temp = sorted(strng.split())
    result = sorted(temp, key=digitsum)
    return " ".join(result)
