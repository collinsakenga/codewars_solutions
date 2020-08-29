def find_ball(scales):
    leftPan = [0, 1, 2]
    rightPan = [5, 6, 7]
    w = scales.get_weight(leftPan, rightPan)
    if w == -1:
        res = leftPan.copy()
    elif w == 1:
        res = rightPan.copy()
    else:
        res = [3, 4]
    leftPan = res[0:1]
    rightPan = res[-1:]
    w = scales.get_weight(leftPan, rightPan)
    if w == 0:
        return res[1]
    elif w == -1:
        return leftPan[0]
    else:
        return rightPan[0]
