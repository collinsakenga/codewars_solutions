def encode(message, key):
    return helper(message, key)
def decode(message, key):
    return helper(message, key)
def helper(message, key):
    dict={j:i for i,j in enumerate(key)}
    dict2={v:k for k,v in dict.items()}
    res=""
    for i in message:
        flag=True if i.isupper() else False
        if i.lower() in dict:
            index=dict[i.lower()]-1 if dict[i.lower()]%2 else dict[i.lower()]+1
            res+=dict2[index].upper() if flag else dict2[index].lower()
        else:
            res+=i    
    return res