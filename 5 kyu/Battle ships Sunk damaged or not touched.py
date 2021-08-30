from copy import deepcopy
movement=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def damaged_or_sunk (board, attacks):
    res={ 'sunk': 0, 'damaged': 0 , 'not_touched': 0, 'points': 0 } 
    memo, dict={}, {}
    for i,j in enumerate(board):
        for k,l in enumerate(j):
            if l!=0 and (i,k) not in memo:
                neighbours=helper(board, i, k, l, {})
                dict[tuple((key for key in neighbours.keys()))]=l
                for key in neighbours.keys():
                    memo[key]=1
    dict2=deepcopy(dict)
    for i,j in attacks:   
        delete=next((k for k in dict.keys() if (len(board)-j, i-1) in k), None)
        if delete==None:
            continue
        dict[delete]-=1
    for i,j,k in zip(dict.values(), dict2.values(), dict.keys()):
        if i==j:
            res["not_touched"]+=1
            res["points"]-=1
        elif (j-i)>=len(k):
            res["sunk"]+=1
            res["points"]+=1
        else:
            res["damaged"]+=1
            res["points"]+=0.5
    return res
def helper(board, y, x, value, record):
    if record.get((y, x), None)!=None:
        return 
    record[(y, x)]=value
    for i,j in movement:
        if valid(board, y+i, x+j) and board[y+i][x+j]==value:
            helper(board, y+i, x+j, value, record)
    return record
def valid(board, i, j):
    if (i<0 or j<0 or i>=len(board) or j>=len(board[0])):
        return False
    return True