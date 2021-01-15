def execute(code):
    pos=x=y=0
    direction=1
    res=[["*"]]
    while pos<len(code):
        temp=""
        if code[pos]=="F":
            pos+=1
            while pos<len(code) and code[pos].isdigit():
                temp+=code[pos]
                pos+=1
            temp=1 if not temp else int(temp)
            if direction==0:
                flag=True
                for i in range(y-1, y-1-temp, -1):
                    if i<0:
                        flag=False
                        res=[list(" "*len(res[0]))]+res
                        res[0][x]="*"
                    else:
                        res[i][x]="*"
                if flag:
                    y-=temp
                else:
                    y=0
            elif direction==1:
                for i in range(x+1, x+temp+1):
                    if i>=len(res[y]):
                        res[y].append("*")
                    else:
                        res[y][i]="*"
                length=len(res[y])
                for i in range(len(res)):
                    res[i]=res[i]+(length-len(res[i]))*[" "]
                x+=temp
            elif direction==2:
                for i in range(y+1, y+temp+1):
                    if i>=len(res):
                        res.append(list(" "*len(res[0])))
                        res[-1][x]="*"
                    else:
                        res[i][x]="*"
                y+=temp
            elif direction==3:
                flag=True
                for i in range(x-1, x-1-temp,-1):
                    if i<0:
                        flag=False
                        res[y]=["*"]+res[y]
                    else:
                        res[y][i]="*"
                if flag:
                    x-=temp
                else:
                    length=len(res[y])
                    for i in range(len(res)):
                        res[i]=(length-len(res[i]))*[" "]+res[i]
                    x=0
        elif code[pos]=="R":
            pos+=1
            while pos<len(code) and code[pos].isdigit():
                temp+=code[pos]
                pos+=1
            temp=1 if not temp else int(temp)
            direction=(direction+temp)%4
        elif code[pos]=="L":
            pos+=1
            while pos<len(code) and code[pos].isdigit():
                temp+=code[pos]
                pos+=1
            temp=1 if not temp else int(temp)
            direction=(direction-temp)%4
    return "\r\n".join("".join(i) for i in res)