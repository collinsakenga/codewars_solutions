def solution(x, y):
    return [x+2, x, x+1][int(y==0)+int(y==1)*2]