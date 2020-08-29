def most_money(students):
    if len(students) == 1:
        return students[0].name
    dict = {}
    for i in students:
        total = i.fives*5+i.tens*10+i.twenties*20
        dict[i.name] = total
    temp = sorted(dict.items(), key=lambda x: -x[1])
    return "all" if temp[0][1] == temp[-1][1] else temp[0][0]
