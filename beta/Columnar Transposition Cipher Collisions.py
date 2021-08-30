from math import ceil
from collections import defaultdict
def columnarCipher(message, cipher, keys):
    res=[]    
    for i in keys:
        table=defaultdict(list)
        for j in range(ceil(len(message)/len(i))):
            for k in range(len(i)):
                index=j*len(i)+k
                if index<len(message):
                    table[i[k]].append(message[index])
        s=""
        for j,k in sorted(table.items(), key=lambda x: x[0]):
            s+="".join(k)
        if s==cipher:
            res.append(i)
    return res