def tick_toward(start, target):
    res=[]
    h_direction=1 if target[0]>=start[0] else -1
    v_direction=1 if target[1]>=start[1] else -1
    times=min(abs(target[0]-start[0]), abs(target[1]-start[1]))
    for i in range(times+1):
        res.append((start[0]+i*h_direction, start[1]+i*v_direction))
    if res[-1][0]==target[0]:
        for i in range(abs(target[1]-res[-1][1])):
            res.append((res[-1][0], res[-1][1]+v_direction))
    elif res[-1][1]==target[1]:
        for i in range(abs(target[0]-res[-1][0])):
            res.append((res[-1][0]+h_direction, res[-1][1]))
    return res