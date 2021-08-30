def find_the_ball(start, swaps):
    for i in swaps:
        if start in i: 
            start=i[i.index(start)-1]
    return start