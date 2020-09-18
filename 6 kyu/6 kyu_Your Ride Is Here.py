def ride(group, comet):
    compare1 = compare2 = 1
    for i in group:
        compare1 *= (ord(i)-ord("A")+1)
    for i in comet:
        compare2 *= (ord(i)-ord("A")+1)
    return "GO" if (compare1 % 47 == compare2 % 47) else "STAY"
