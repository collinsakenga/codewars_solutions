def value_at(poly_spec, x):
    num=1
    total=0
    for i,j in enumerate(poly_spec[::-1]):
        total+=j*num
        num=(num*(x-i))/(i+1)
    return round(total, 2)