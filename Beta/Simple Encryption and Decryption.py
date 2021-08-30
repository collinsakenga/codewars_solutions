def encrypt(st, encryption_dict):
    return "".join(encryption_dict[i] for i in st)
    
def decrypt(st, encryption_dict):
    encryption_dict={j:i for i,j in encryption_dict.items()}
    res=temp=""
    for i in st:
        temp+=i
        if temp in encryption_dict:
            res+=encryption_dict[temp]
            temp=""
    return res
