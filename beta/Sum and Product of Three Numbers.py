def number_of_sets(a, b):
    count = 0
    for x in range(1,1000):
        if x > a: break
        for y in range(x,1000):
            if x + y > a: break
            z1 = a - (x+y); z2 = b/(x*y)
            if z1 == z2 and x <= y <= z1: count += 1
    return count