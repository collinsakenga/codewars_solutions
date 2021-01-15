dict1={i:j for i,j in enumerate("abcdefghijklmnopqrstuvwxyz")}
dict2={j:i for i,j in dict1.items()}
def encode_str(strng, shift):
    shift=shift%26
    first=strng[0].lower()
    strng=first+dict1[(ord(first)-ord("a")+shift)%26]+strng  
    if len(strng)%5==0:
        split=[len(strng)//5 for i in range(5)]
    else:
        length=len(strng)//4
        temp=len(strng)-length*4
        while temp+4<length:
            temp+=4
            length-=1
        split=[length]*4+[temp]
    res=""
    for i,j in enumerate(strng):
        if i<2 or not j.isalpha():
            res+=j
            continue
        char=dict1[(ord(j.lower())-ord("a")+shift)%26]
        res+=char if j.islower() else char.upper()
    index=0
    arr=[]
    for j in (k for k in split if k):
        arr.append(res[index:j+index])
        index+=j
    return arr
def decode(arr):
    diff=-(ord(arr[0][1])-ord(arr[0][0]))
    arr[0]=arr[0][2:]
    res=""
    for i in arr:
        for j in i:
            if not j.isalpha():
                res+=j
                continue
            char=dict1[(ord(j.lower())-ord("a")+diff)%26]
            res+=char if j.islower() else char.upper()
    return res