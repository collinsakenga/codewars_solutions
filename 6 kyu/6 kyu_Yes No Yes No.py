def yes_no(arr):
    res = []
    flag = 0
    count = 0
    while arr:
        for i in range(count, len(arr), 2):
            res.append(arr[i])
            count += 1
        temp = arr.copy()
        for i in range(count-flag):
            arr.pop(i+flag)
        count = 0 if res[-1] != temp[-1] else 1
        if count == 1:
            flag = 1
        else:
            flag = 0
    return res
