from heapq import *
moves=[(0, 1), (0, -1), (-1, 0), (1, 0)]
def path_finder(area):
    map=[[int(j) for j in i] for i in area.split("\n")]
    edge=(len(map)-1, len(map[0])-1)
    res=[(0, (0, 0))]
    memo=set() 
    while res:
        cost, location=heappop(res)
        if location==edge: 
            return cost 
        elif location in memo:
            continue
        memo.add(location)
        for i,j in moves:
            y, x=location[0]+i, location[1]+j
            if (y, x) not in memo and (0<=y<=edge[0] and 0<=x<=edge[1]):
                cost_new=cost+abs(map[location[0]][location[1]]-map[y][x])
                heappush(res, (cost_new, (y, x)))
    return 0