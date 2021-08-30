def loneliest(number): 
    temp=str(number)
    if '1' not in temp:
        return False
    res=[]
    record=[]
    for i,num in enumerate(temp):
        seen=int(num)
        string=""
        for j in range(i-1, max(-1, i-1-seen),-1):
            string+=temp[j]
        for j in range(i+1, min(len(temp), i+1+seen)):
            string+=temp[j]
        if not res:
            res.append(string)
            record.append(seen)
        elif digit_sum(res[0])>digit_sum(string):
            res=[string]
            record=[seen]
        elif digit_sum(res[0])==digit_sum(string):
            res.append(string)
            record.append(seen)
    return True if 1 in record else False
def digit_sum(s):
    return sum(int(i) for i in s)