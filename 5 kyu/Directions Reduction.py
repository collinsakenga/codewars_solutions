def dirReduc(testing):
    list_len=len(testing)
    index=loop=comp=0
    while True:
        if list_len<=1:
            break
        if index>=list_len-1:
            index=0
            total=len(testing)
            if comp==total:
                break
            if total!=comp:
                comp=total
        if testing[index+1]=="NORTH" and testing[index]=="SOUTH":
            del testing[index:index+2]
            list_len-=2
        elif testing[index+1]=="SOUTH" and testing[index]=="NORTH":
            del testing[index:index+2]
            list_len-=2
        elif testing[index+1]=="EAST" and testing[index]=="WEST":
            del testing[index:index+2]
            list_len-=2
        elif testing[index+1]=="WEST" and testing[index]=="EAST":
            del testing[index:index+2]
            list_len-=2
        else:
            index+=1
    return testing