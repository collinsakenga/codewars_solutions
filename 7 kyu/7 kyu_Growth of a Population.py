def nb_year(p0, percent, aug, p):
    count = 0
    while p > p0:
        count += 1
        p0 = p0+p0*percent/100 + aug
    return count
