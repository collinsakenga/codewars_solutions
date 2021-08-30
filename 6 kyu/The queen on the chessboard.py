def available_moves(position):
    if not isinstance(position, str) or len(position)!=2:
        return []
    number=int(position[1:])
    if not (number>=1 and number<=8) or  not (position[0] in "ABCDEFGH"):
        return []
    res=set()
    for i in range(1, 9):
        res.add(f"{position[0]}{i}")
    for i in range(8):
        temp=chr(ord("A")+i)
        res.add(f"{temp}{number}")
    for i in range(1, 8):
        temp1=ord(position[0])+i
        temp2=number+i
        temp3=ord(position[0])-i
        temp4=number-i
        if not (temp1>ord("H") or temp2>8):
            res.add(f"{chr(temp1)}{temp2}")
        if not (temp3<ord("A") or temp2>8):
            res.add(f"{chr(temp3)}{temp2}")
        if not (temp1>ord("H") or temp4<=0):
            res.add(f"{chr(temp1)}{temp4}")
        if not (temp3<ord("A") or temp4<=0):
            res.add(f"{chr(temp3)}{temp4}")
    final=sorted(res)
    final.remove(position)
    return final