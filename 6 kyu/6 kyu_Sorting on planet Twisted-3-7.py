def sort_twisted37(arr):
    return sorted(arr, key=lambda x: convert(x))


def convert(n):
    if "3" not in str(n) and "7" not in str(n):
        return n
    neg_flag = True if n < 0 else False
    n = abs(n)
    total = 0
    for i in str(n):
        if i == "3":
            total = total*10+7
        elif i == "7":
            total = total*10+3
        else:
            total = total*10+int(i)
    return -total if neg_flag else total
