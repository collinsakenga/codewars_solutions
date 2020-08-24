def who_is_next(names, r):
    result = []
    temp = len(names)
    for num in range(1, temp+1):
        result.append(num)
    n = 0
    while True:
        if result[temp-1] >= r:
            break
        for j in range(0, temp):
            result[j] += (temp+j)*2**n
        n += 1
    for i in range(0, temp-1):
        if result[i] <= r and result[i+1] > r:
            return names[i]
    return names[temp-1]
