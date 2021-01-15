def cockroaches(room):
    res=[0]*10
    locations=[(i, k) for i,j in enumerate(room) for k,l in enumerate(j) if l in "UDLR"]
    x, y=len(room[0])-1, len(room)-1
    for i in locations:
        temp=[None]*5
        if room[i[0]][i[1]]=="U":
            x2, y2=i[1], 0
            temp[0]=next((room[0][k] for k in range(x2, -1, -1) if room[0][k].isdigit()), None)
            temp[1]=next((room[k][0] for k in range(0, y+1) if room[k][0].isdigit()), None)
            temp[2]=next((room[y][k] for k in range(0, x+1) if room[y][k].isdigit()), None)
            temp[3]=next((room[k][x] for k in range(y, -1, -1) if room[k][x].isdigit()), None)
            temp[4]=next((room[0][k] for k in range(x, x2, -1) if room[0][k].isdigit()), None)
        elif room[i[0]][i[1]]=="D":
            x2, y2=i[1], y 
            temp[0]=next((room[y][k] for k in range(x2, x+1) if room[y][k].isdigit()), None)
            temp[1]=next((room[k][x] for k in range(y, -1, -1) if room[k][x].isdigit()), None)
            temp[2]=next((room[0][k] for k in range(x, -1, -1) if room[0][k].isdigit()), None)
            temp[3]=next((room[k][0] for k in range(0, y+1) if room[k][0].isdigit()), None)
            temp[4]=next((room[y][k] for k in range(0, x2) if room[y][k].isdigit()), None)
        elif room[i[0]][i[1]]=="L":
            x2, y2=0, i[0]
            temp[0]=next((room[k][0] for k in range(y2, y+1) if room[k][0].isdigit()), None)
            temp[1]=next((room[y][k] for k in range(0, x) if room[y][k].isdigit()), None)
            temp[2]=next((room[k][x] for k in range(y, -1, -1) if room[k][x].isdigit()), None)
            temp[3]=next((room[0][k] for k in range(x, -1, -1) if room[0][k].isdigit()), None)
            temp[4]=next((room[k][0] for k in range(0, y2) if room[k][0].isdigit()), None)
        elif room[i[0]][i[1]]=="R":
            x2, y2=x, i[0]
            temp[0]=next((room[k][x] for k in range(y2, -1, -1) if room[k][x].isdigit()), None)
            temp[1]=next((room[0][k] for k in range(x, -1, -1) if room[0][k].isdigit()), None)
            temp[2]=next((room[k][0] for k in range(0, y+1) if room[k][0].isdigit()), None)
            temp[3]=next((room[y][k] for k in range(0, x+1) if room[y][k].isdigit()), None)
            temp[4]=next((room[k][x] for k in range(y, y2, -1) if room[k][x].isdigit()), None)
        if temp[0]!=None:
            res[int(temp[0])]+=1
        elif temp[1]!=None:
            res[int(temp[1])]+=1
        elif temp[2]!=None:
            res[int(temp[2])]+=1
        elif temp[3]!=None:
            res[int(temp[3])]+=1
        elif temp[4]!=None:
            res[int(temp[4])]+=1
    return res