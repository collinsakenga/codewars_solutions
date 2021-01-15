def meeting(rooms, number):
    if number==0:
        return "Game On"
    res=[]
    for i in rooms:
        res.append(i[1]-len(i[0])) if i[1]>len(i[0]) else res.append(0)
        if sum(res)>=number:
            return res[:-1]+[number-sum(res[:-1])]
    return "Not enough!"