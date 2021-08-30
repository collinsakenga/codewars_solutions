def solution(string,markers):  
    temp=[]
    s=""
    for i in string.split("\n"):
        for c in i:
            if c in markers:
                break
            s+=c
        temp.append(s.rstrip())
        s=""
    return "\n".join(temp)