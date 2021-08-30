from itertools import product
def is_divisible_by_6(string):
    if string[-1]!="*" and int(string[-1])%2:
        return []
    temp=list(string)
    index=[i for i,j in enumerate(temp) if j=="*"]
    res=[]
    for sequence in product("0123456789", repeat=len(index)):
        replace="".join(sequence)
        number=temp.copy()
        for i,j in enumerate(index):
            number[j]=replace[i]
        if int(number[-1])%2==0 and digit_sum("".join(number))%3==0:
            res.append("".join(number))
    return res
def digit_sum(s):
    return sum(int(i) for i in s)