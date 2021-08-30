from collections import deque
dict={'^': {(0, 1): ["R",'F'], (0, -1): ["L",'F'], (-1, 0): ['F'], (1, 0): ["B",'F']}, 
      'v': {(0, 1): ["L",'F'], (0, -1): ["R",'F'], (-1, 0): ["B",'F'], (1, 0): ['F']}, 
      '<': {(0, 1): ["B",'F'], (0, -1): ['F'], (-1, 0): ["R",'F'], (1, 0): ["L",'F']}, 
      '>': {(0, 1): ['F'], (0, -1): ["B",'F'], (-1, 0): ["L",'F'], (1, 0): ["R",'F']}}
direction={(0, 1): ">", (0, -1): "<", (-1, 0): "^", (1, 0): "v"}
moves=[(0, 1), (0, -1), (-1, 0), (1, 0)]
def escape(maze):
    start=next((i, k) for i,j in enumerate(maze) for k,l in enumerate(j) if l in ">^<v")
    res=deque([(start[0], start[1], [], maze[start[0]][start[1]])])
    edge=[0, len(maze)-1, 0, len(maze[0])-1]
    memo=set()
    while res:
        location=res.popleft()
        if location[0] in edge[:2] or location[1] in edge[2:]:
            return location[2]
        elif location[:2] in memo:
            continue
        memo.add(location[:2])
        for i,j in moves:
            y, x=location[0]+i, location[1]+j
            if ((y, x) not in memo) and (0<=y<=edge[1] and 0<=x<=edge[3]) and (maze[y][x]==" "):
                arr=location[2]+dict[location[3]][(i, j)]
                cur=direction[(i, j)]
                res.append((y, x, arr, cur))
    return []