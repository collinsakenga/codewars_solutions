def queens(position, size):
    pos=(ord(position[0])-ord("a"), int(position[1:])-1 if position[1:]!="0" else 9)
    temp=helper([pos], 0, {pos[0]}, {pos[1]}, {pos[1]-pos[0]}, {pos[0]+pos[1]}, [], size, pos[0])
    res=[]
    for i,j in temp[0]:
        res.append(f"{chr(ord('a')+i)}{(j+1)%10}")
    return ",".join(res)
def helper(cur, num, row, col, diag1, diag2, memo, target, dismiss):
    if len(cur)==target:
        memo.append(cur)
        return memo
    for i in range(target):
        if (num not in row) and (i not in col) and (i-num not in diag1) and (i+num not in diag2):
            helper(cur+[(num, i)], num+1, row|{num}, col|{i}, diag1|{i-num}, diag2|{i+num}, memo, target, dismiss)
    if num==dismiss:
        helper(cur, num+1, row, col, diag1, diag2, memo, target, dismiss)
    return memo