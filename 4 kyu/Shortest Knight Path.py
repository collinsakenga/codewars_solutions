from collections import deque
dict={j:i for i,j in enumerate("abcdefgh")}
movement=[(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (-2, -1), (-1, -2), (1, -2)]
def knight(p1, p2):
    l1=[dict[p1[0]], int(p1[1])-1, 0]
    l2=[dict[p2[0]], int(p2[1])-1]
    res=deque([l1])
    visited=set()
    while res:
        location=res.popleft()
        if location[0]==l2[0] and location[1]==l2[1]:
            return location[-1]
        visited.add((location[0], location[1]))
        for i,j in movement:
            if (location[0]+i, location[1]+j) not in visited and valid(location[0]+i, location[1]+j):
                res.append((location[0]+i, location[1]+j, location[2]+1))
def valid(y, x):
    if (y<0 or x<0 or y>7 or x>7):
        return False
    return True
        
    