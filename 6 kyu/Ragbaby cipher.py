from collections import Counter
def encode(text, key):
    return helper(text, key, True)
def decode(text, key): 
    return helper(text, key, False)
def helper(text, key, flag):
    dict={j:i for i,j in enumerate(Counter(key+"abcdefghijklmnopqrstuvwxyz").keys())}
    dict2={v:k for k,v in dict.items()}
    res=""
    count=0
    for k in text:
        if k.lower() in dict:
            count+=1
            index=(dict[k.lower()]+(count if flag else -count))%26
            res+=dict2[index].upper() if k.isupper() else dict2[index].lower()
        else:
            res+=k
            count=0
    return res