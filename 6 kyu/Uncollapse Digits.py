check={'one', 'four', 'five', 'three', 'nine', 'two', 'zero', 'six', 'seven', 'eight'}
def uncollapse(digits):
    res=[]
    temp=""
    for i in digits+" ":
        if temp in check:
            res.append(temp)
            temp=i
        else:
            temp+=i
    return " ".join(res)
    