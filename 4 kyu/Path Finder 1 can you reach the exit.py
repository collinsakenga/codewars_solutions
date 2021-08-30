import sys
sys.setrecursionlimit(10000)
movements=[(1, 0), (-1, 0), (0, 1), (0, -1)]
def path_finder(maze):
    map_=maze.split("\n")
    return helper(map_, len(map_)-1, len(map_[0])-1, set())
def helper(map_, y, x, memo):
    if map_[y][x]=="W":
        return False
    elif y==x==0:
        return True
    elif (y, x) in memo:
        return False
    memo.add((y, x))
    return any(helper(map_, y+i, x+j, memo) for i,j in movements if valid(map_, y+i, x+j))
def valid(map_, y, x):
    if (y<0 or x<0 or y>=len(map_) or x>=len(map_[0])):
        return False
    return True