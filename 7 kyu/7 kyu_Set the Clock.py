def set_clock(time, buttons):
    res=[int(time.split(":")[0]), int(time.split(":")[1])]
    for i in buttons:
        if i=="M":
            res[1]=(res[1]+1)%60
        elif i=="H":
            res[0]=(res[0]+1)%24
    return "{:d}:{:02d}".format(res[0] if res[0] else 24, res[1])