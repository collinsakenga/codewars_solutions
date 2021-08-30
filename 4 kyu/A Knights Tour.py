moves=((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
def knights_tour(start, size):
    temp=helper(start[0], start[1], size, size**2, set())
    return [tuple(i) for i in [start]+temp]
def helper(y, x, size, total, memo):
    temp=[]
    memo.add((y, x))
    for i,j in moves:
        new_y, new_x=y+i, x+j
        if not valid(size, new_y, new_x) or (new_y, new_x) in memo:
            continue
        count=sum(valid(size, new_y+k, new_x+l) and (new_y+k, new_x+l) not in memo for k,l in moves)
        temp.append((new_y, new_x, count))
    if not temp:
        return []
    temp=sorted(temp, key=lambda x: x[-1])
    temp=temp[:next((i for i,j in enumerate(temp) if j[-1]!=temp[0][-1]), len(temp))]
    temp=list(sorted(temp, key=lambda x: center(size//2, x[0], x[1]))[-1][:2])
    return [temp]+helper(temp[0], temp[1], size, total, memo)
def center(size, y, x):
    return max(abs(y-i)+abs(j-x) for i in range(size-1, size+1) for j in range(size-1, size+1))
def valid(size, y, x):
    if y<0 or x<0 or y>=size or x>=size:
        return False
    return True