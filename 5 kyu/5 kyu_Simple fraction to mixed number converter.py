def mixed_fraction(s):
    temp = s.split("/")
    up = int(temp[0])
    down = int(temp[1])
    if down == 0:
        raise ZeroDivisionError
    if up == 0:
        return "0"
    flag = up < 0 or down < 0 if not (up < 0 and down < 0) else False
    up = abs(up)
    down = abs(down)
    quotient = up//down
    res = ""
    if flag:
        res += "-"
    if quotient > 0 and up % down == 0:
        return res+str(quotient)
    up -= quotient*down
    factor = 2
    while factor < int(sqrt(down))+1:
        if up % factor == 0 and down % factor == 0:
            up = up//factor
            down = down//factor
            factor = 1
        factor += 1
    if quotient > 0:
        return f"{res}{quotient} {up}/{down}"
    return f"{res}{up}/{down}"
