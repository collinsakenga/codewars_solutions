key="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&"+'"'
def decrypt(encrypted_text):
    if not encrypted_text: return encrypted_text
    encrypted_text=list(key[77-key.index(encrypted_text[0])-1]+encrypted_text[1:])
    res=encrypted_text[0]
    for i,j in enumerate(encrypted_text):
        if i==0: continue
        try:
            res+=key[key.index(encrypted_text[i-1])-key.index(encrypted_text[i])] if (i+1)%2!=0 else key[key.index(encrypted_text[i-1])-key.index(encrypted_text[i])].swapcase()
        except:
            raise Exception()
        encrypted_text[i]=res[i].swapcase() if (i+1)%2==0 else res[i]
    return res
def encrypt(text):
    if not text: return text
    rec=text[0]
    temp=list(text)
    res=""
    for i,j in enumerate(temp):
        if (i+1)%2==0:
            temp[i]=j.swapcase()
        try:
            res+=key[key.index(temp[i-1])-key.index(temp[i])]
        except:
            raise Exception()
    res=key[77-key.index(rec)-1]+res[1:]
    return res