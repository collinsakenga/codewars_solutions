def queue_time(customers, n):
    if not customers:
        return 0
    elif n == 1:
        return sum(customers)
    elif n > len(customers):
        return max(customers)
    list = []
    for i in range(0, n):
        list.append(customers[i])
    for i in range(n, len(customers)):
        list[list.index(min(list))] += customers[i]
    return max(list)
