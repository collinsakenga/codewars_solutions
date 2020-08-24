def snail(snail_map):
    if len(snail_map) == 1:
        return snail_map[0]
    up = 0
    low = len(snail_map)
    left = 0
    right = len(snail_map)
    total = 0
    result = []
    while total < len(snail_map)**2:
        for i in range(left, right):
            result.append(snail_map[up][i])
            total += 1
        right -= 1
        for i in range(up+1, low):
            result.append(snail_map[i][right])
            total += 1
        low -= 1
        for i in range(right-1, left-1, -1):
            result.append(snail_map[low][i])
            total += 1
        up += 1
        for i in range(low-1, up-1, -1):
            result.append(snail_map[i][left])
            total += 1
        left += 1
    return result
