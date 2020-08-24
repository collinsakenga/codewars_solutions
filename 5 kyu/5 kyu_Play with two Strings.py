def work_on_strings(a, b):
    temp3 = ""
    temp4 = ""
    for i in b:
        if (a.count(i.upper())+a.count(i.lower())) % 2 != 0:
            if i.isupper():
                temp3 += i.lower()
            else:
                temp3 += i.upper()
        else:
            temp3 += i
    for i in a:
        if (b.count(i.upper())+b.count(i.lower())) % 2 != 0:
            if i.isupper():
                temp4 += i.lower()
            else:
                temp4 += i.upper()
        else:
            temp4 += i
    return temp4+temp3
