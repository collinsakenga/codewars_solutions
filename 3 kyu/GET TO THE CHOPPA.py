from queue import *
from copy import deepcopy
movement=[(1, 0), (-1, 0), (0, 1), (0, -1)]
def find_shortest_path(grid, start_node, end_node):
    if not grid:
        return []
    arr=PriorityQueue()
    start=(start_node.position.y, start_node.position.x)
    end=(end_node.position.y, end_node.position.x)
    arr.put((0, (start[0], start[1], 0, [(start[1], start[0])])))
    res=print_grid(grid, start_node, end_node).split("\n")
    went=set()
    while not arr.empty():
        pos=arr.get()[1]
        if (pos[0], pos[1]) in went:
            continue
        if (pos[0], pos[1])==end:
            dict={(j.position.x, j.position.y):j for i in grid for j in i}
            return [dict[i] for i in pos[-1]]
        went.add((pos[0], pos[1]))
        for i,j in movement:
            y, x=pos[0]+i, pos[1]+j
            if valid(res, y, x) and (y, x) not in went and res[y][x] in "0E":
                diff=pos[2]+1+distance(y, x, end[0], end[1])
                arr.put((diff, (y, x, pos[2]+1, pos[-1]+[(x, y)])))
    return []
def distance(i,j, y, x):
    return abs(i-y)+abs(j-x)
def valid(res, y, x):
    if y<0 or x<0 or y>=len(res) or x>=len(res[y]):
        return False
    return True