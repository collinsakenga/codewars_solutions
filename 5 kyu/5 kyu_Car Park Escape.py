def escape(carpark):
    start = next(([i, j] for i in range(len(carpark))
                  for j in range(len(carpark[i])) if carpark[i][j] == 2))
    res = []
    vertical = start[0]
    horizontal = start[1]
    length = len(carpark[0])-1
    last = len(carpark)-1
    while vertical != last:
        one = next(
            (i for i in range(len(carpark[vertical])) if carpark[vertical][i] == 1))
        res.append(
            f"R{one-horizontal}") if one > horizontal else res.append(f"L{horizontal-one}")
        horizontal = one
        temp = vertical
        while vertical < last and carpark[vertical][horizontal] == 1:
            vertical += 1
        res.append(f"D{vertical-temp}")
    return res if horizontal == length else res+[f"R{length-horizontal}"]