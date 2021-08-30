pos=[0, 0]
check={}
def i_am_here(path):
    res=[]
    temp=""
    for i in path+"_":
        if i.isdigit():
            temp+=i
            continue
        mod=(check.get("l", 0)-check.get("r", 0)+(check.get("L", 0)-check.get("R", 0))*2)%4
        if mod==3:
            pos[1]+=int(temp or "0")
        elif mod==1:
            pos[1]-=int(temp or "0")
        elif mod==2:
            pos[0]+=int(temp or "0")
        else:
            pos[0]-=int(temp or "0")
        check[i]=check.get(i, 0)+1
        temp=""
    return pos