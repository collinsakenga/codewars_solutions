from collections import deque
movements=[(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1)]
def path_finder(maze):
    map_=maze.split("\n")
    res=deque([(len(map_)-1, len(map_[0])-1, 0)])
    visited=set()
    while res:
        location=res.popleft()
        if (location[0], location[1]) in visited or map_[location[0]][location[1]]=="W":
            continue
        visited.add((location[0], location[1]))
        if location[0]==location[1]==0:
            return location[2]
        for i,j,k in movements:      
            if valid(map_, location[0]+i, location[1]+j):
                res.append((location[0]+i, location[1]+j, location[2]+1))
    return False
def valid(map_, y, x):
    if (y<0 or x<0 or y>=len(map_) or x>=len(map_[0])):
        return False
    return True