def bocce_score(balls):
    red=[]
    black=[]
    distance=sum([i["distance"] for i in balls if i["type"]=="jack"], ())
    for i in balls:
        if i["type"]=="red":
            red.append((distance[0]-i["distance"][0])**2+(distance[1]-i["distance"][1])**2)
        elif i["type"]=="black":
            black.append((distance[0]-i["distance"][0])**2+(distance[1]-i["distance"][1])**2)
    red.sort()
    black.sort()
    index=0
    if red[0]==black[0]:
        return 'No points scored'
    elif red[0]>black[0]:
        while index<len(black) and black[index]<red[0]:
            index+=1
        return "black scores "+str(index)
    else:
        while index<len(red) and red[index]<black[0]:
            index+=1
        return "red scores "+str(index)