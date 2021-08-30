def find_additive_numbers(num):
    for i in range(len(num)-2):
        first=num[:i+1]
        for j in range(i+1, len(num)-1):
            second=num[i+1:j+1]
            remain=num[j+1:]
            if (int(first)+int(second))>int(remain):
                break
            temp=helper(remain, int(first), int(second), [first, second])
            if not temp or len(temp)<=2:
                continue
            flag=True
            for k in range(len(temp)-2):
                if int(temp[k])+int(temp[k+1])!=int(temp[k+2]):
                    flag=False 
                    break 
            if flag and all(k[0]!="0" or (k[0]=="0" and len(k)==1) for k in temp):
                return temp
    return []
def helper(num, first, second, arr=[]):
    if num=="":
        return arr 
    elif first+second>int(num):
        return None
    res=str(first+second)
    for i,j in enumerate(num):
        temp=num[:i+1]
        if temp.startswith("0") and i!=0 or temp[i]!=res[i]:
            break 
        elif (first+second)==int(temp): 
            return helper(num[i+1:], second, int(temp), arr+[temp])
    arr[-1]+=num[0]
    return helper(num[1:], first, second*10+int(num[0]), arr)