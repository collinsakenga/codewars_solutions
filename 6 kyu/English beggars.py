def beggars(values, n):
    return [sum(values[j] for j in range(i, len(values), n)) for i in range(n)]