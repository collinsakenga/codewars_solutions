def reverse_in_parentheses(s):
    res=""
    arr=[]
    for i in s:
        if i=="(":
            arr.append("")
        elif i==")":
            temp=arr.pop()[::-1]
            if not arr:            
                res+="("+temp+")"
            else:
                arr[-1]+=")"+temp+"(" if len(arr)%2 else "("+temp+")"
        else:
            if arr:
                arr[-1]+=i
            else:
                res+=i
    return res