def compare(a, b):
    if a=="*" and b=="*":
        return b
    elif a=="*":
        return b
    elif b=="*":
        return a
    spec_a, spec_b=[0,0,0], [0,0,0]
    for i in a.split():
        if not (i[0] in ".#"):
            spec_a[2]+=1
        spec_a[0]+=i.count("#")
        spec_a[1]+=i.count(".")
    for i in b.split():
        if not (i[0] in ".#"):
            spec_b[2]+=1  
        spec_b[0]+=i.count("#")
        spec_b[1]+=i.count(".")
    if spec_a[0]>spec_b[0]:
        return a
    elif spec_b[0]>spec_a[0]:
        return b
    else:
        if spec_a[1]>spec_b[1]:
            return a
        elif spec_b[1]>spec_a[1]:
            return b
        else:
            if spec_a[2]>spec_b[2]:
                return a
            elif spec_b[2]>spec_a[2]:
                return b
            return b