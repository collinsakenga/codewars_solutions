dict={"6":"9", "1":"1", "0":"0", "8":"8", "9":"6"}
def solve(a, b):
    count=0
    for i in range(a, b):
        temp=str(i)[::-1]
        temp2=""
        flag=False
        for j in temp:
            try:
                temp2+=dict[j]
            except:
                flag=True
                break
        if flag:
            continue
        if temp2==str(i):
            count+=1
    return count