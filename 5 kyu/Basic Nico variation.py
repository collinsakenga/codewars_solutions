from functools import reduce
def nico(key, message):
    temp=[[] for i in range(len(key))]
    for i in range(len(message)):
        temp[i%len(key)].append(message[i])
    maxlen=len(temp[0])
    dict={}
    for i in range(len(temp)):
        dict[key[i]]=temp[i]
    res=sorted(dict.items(), key=lambda x:(ord(x[0])))
    for i in range(len(res)):
        res[i]=list(res[i])
        res[i].pop(0)
        res[i]=reduce(lambda x : x, res[i])
        if len(res[i])<maxlen:
            res[i]+=[" "]
        elif not res[i]:
            res[i]=[" "]
    string=""
    for j in range(len(res[0])):
        for i in range(len(res)):
            string+=res[i][j]
    return string