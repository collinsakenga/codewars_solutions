from collections import Counter
from math import factorial
def anagram_counter(words):
    if not words:
        return 0
    dict={}
    for i in words:
        flag=True
        for j in dict.keys():
            if Counter(j)==Counter(i):
                dict[j]+=1
                flag=False
                break
        if flag:
            dict[i]=1
    total=0
    for i in dict.values():
        if i>=2:
            total+=combo(i)
    return total
def combo(n):
    return factorial(n)//(factorial(2)*factorial(n-2))