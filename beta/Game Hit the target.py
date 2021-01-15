def solution(mtrx):
    return any("".join(j for j in i if j in ">x")==">x" for i in mtrx)