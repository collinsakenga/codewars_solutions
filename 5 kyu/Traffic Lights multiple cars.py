def traffic_lights(road, n):
    table={i:j for i,j in enumerate(road)}
    res=[road]
    cur=["." if j=="C" else j for j in road]
    cars=[i for i,j in enumerate(road) if j=="C"][::-1]
    for second in range(1, n+1):
        for j in range(len(cur)-1, -1, -1):
            if table[j]=="G":
                cur[j]="G" if second%11<5 else "O" if second%11==5 else "R"
            elif table[j]=="R":
                cur[j]="R" if second%11<5 else "G" if second%11<10 else "O"
            elif table[j]=="O": 
                cur[j]="R" if second%11<6 else "G" if second%11<11 else "O"
        temp_cars=[]
        for pos in cars:
            if pos==len(cur)-1:
                continue
            if cur[pos]=="R" or cur[pos+1] in "RO" or (pos+1) in temp_cars or (pos+1 in cars and (cur[pos+1]=="G" and pos+1!=len(cur)-1)):
                temp_cars.append(pos)
            elif cur[pos+1] in "G":
                next_light=next((c for c in range(pos+2, len(cur)) if cur[c] in "ROG"), None)
                temp_cars.append(pos) if next_light and all(c in temp_cars for c in range(pos+2, next_light)) else temp_cars.append(pos+1)
            else:
                temp_cars.append(pos+1)
        res.append("".join(cur[index] if (index not in temp_cars) else "C" for index in range(len(cur))))
        cars=temp_cars 
    return res 