movement=[(1, 0, "right"), (-1, 0, "left"), (0, 1, "down"), (0, -1, "up")]
def solve(map, miner, exit):
    return helper(map, miner["x"], miner["y"], exit["x"], exit["y"], set())
def helper(map, cur_y, cur_x, target_y, target_x, went):
    if cur_y==target_y and cur_x==target_x:
        return []
    flag=(cur_y, cur_x) in went
    went.add((cur_y, cur_x))
    if not flag:
        for i,j,k in movement:
            if valid(map, cur_y+i, cur_x+j) and map[cur_y+i][cur_x+j]==True and (cur_y+i, cur_x+j) not in went:
                return [k]+helper(map, cur_y+i, cur_x+j, target_y, target_x, went)
    return []
def valid(map, y, x):
    if (y<0 or x<0 or y>=len(map) or x>=len(map[y])):
        return False
    return True