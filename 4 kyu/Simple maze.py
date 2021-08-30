from queue import PriorityQueue
moves=[(0, 1), (0, -1), (-1, 0), (1, 0)]
def has_exit(maze):
    if sum(j=="k" for i in maze for j in i)!=1:
        raise Exception()
    res=PriorityQueue()
    start=next((i, k) for i,j in enumerate(maze) for k,l in enumerate(j) if l=="k")
    res.put((0,(start[0],start[1])))
    edge=[0, len(maze)-1, 0, len(maze[0])-1]
    memo=set()
    while not res.empty():
        location=res.get()
        if location[1][0] in edge[:2] or location[1][1] in edge[2:]:
            return True
        elif location[1] in memo:
            continue
        memo.add(location[1])
        for i,j in moves:
            y, x=location[1][0]+i, location[1][1]+j
            if (0<=y<=edge[1] and 0<=x<=edge[3]) and maze[y][x]==" ":
                res.put((location[0]+1,(y,x)))
    return False