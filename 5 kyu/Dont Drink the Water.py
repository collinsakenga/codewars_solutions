def separate_liquids(glass):
    if not glass: return []
    count=[0]*4
    for i in glass:
        count[0]+=i.count("O")
        count[1]+=i.count("A")
        count[2]+=i.count("W")
        count[3]+=i.count("H")
    res=[[""]*len(glass[i]) for i in range(len(glass))]
    for i in range(len(res)):
        for j in range(len(res[i])):
            if count[0]:
                res[i][j]="O"
                count[0]-=1
            elif count[1]:
                res[i][j]="A"
                count[1]-=1
            elif count[2]:
                res[i][j]="W"
                count[2]-=1
            elif count[3]:
                res[i][j]="H"
                count[3]-=1
    return res