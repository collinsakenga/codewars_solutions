def exchange_with(a, b):
    a.reverse()
    b.reverse()
    temp = b.copy()
    temp2 = a.copy()
    b.clear()
    for i in temp2:
        b.append(i)
    a.clear()
    for i in temp:
        a.append(i)
