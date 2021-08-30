def validate_battlefield(field):
    total=sum(sum(i) for i in field)
    if total!=20:
        return False
    return True if battleship(field)==1 and cruiser(field)==2 and destroyer(field)==3 and submarine(field)==4 else False
def battleship(field):
    return general_horizontal(4, field)+general_vertical(4, field)
def cruiser(field):
    return general_horizontal(3, field)+general_vertical(3, field)
def destroyer(field):
    return general_horizontal(2, field)+general_vertical(2, field)
def submarine(field):
    return general_vertical(1, field)
def general_vertical(length, field):
    count=0
    for i in range(len(field)-length+1):
        for j in range(len(field[i])):
            flag=True
            for check in range(i, i+length):
                if field[check][j]==0:
                    flag=False
                    break
            if not flag: continue
            for k in range(i-1, i+length+1):
                for l in range(j-1, j+2):
                    if (k<0 or l<0 or k>=len(field) or l >=len(field[i]) or (l==j and (k>=i and k<=(i+length-1)))):
                        continue
                    elif field[k][l]==1:
                        flag=False
            if flag:
                count+=1
    return count
def general_horizontal(length, field):
    count=0
    for i in range(len(field)):
        for j in range(len(field[i])-length+1):
            flag=True
            for check in range(j, j+length):
                if field[i][check]==0:
                    flag=False
                    break
            if not flag: continue
            for k in range(i-1, i+2):
                for l in range(j-1, j+length+1):
                    if (k<0 or l<0 or k>=len(field) or l>=len(field[i]) or (k==i and (l>=j and l<=(j+length-1)))):
                        continue
                    elif field[k][l]==1:
                        flag=False
            if flag:
                count+=1
    return count