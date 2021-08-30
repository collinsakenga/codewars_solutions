def death_star(week):
    res=[0]*3
    require=(100, 75, 50)
    for i in week[:week[-1]]:
        for index,j in enumerate(i):
            res[index]+=j
    if any(require[i]>j for i,j in enumerate(res)):
        remain=tuple(max(0, j-i) for i,j in zip(res, require))
        return 'The station is destroyed!'+" It needed {} iron, {} steel and {} chromium for completion.".format(*remain)
    return 'The station is completed!'