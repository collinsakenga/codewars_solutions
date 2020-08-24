def tickets(people):
    if people[0] != 25:
        return "NO"
    arr = [0, 0, 0]
    for i in people:
        if i == 25:
            arr[0] += 1
        elif i == 50:
            arr[0] -= 1
            if arr[0] < 0:
                return "NO"
            arr[1] += 1
        elif i == 100:
            if arr[0] >= 3 and arr[1] == 0:
                arr[0] -= 3
            elif arr[0] >= 1 and arr[1] >= 1:
                arr[0] -= 1
                arr[1] -= 1
            else:
                return "NO"
    return "YES"
