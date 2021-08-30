def decrypt(encrypted_text, n):
    if n<1:
        return encrypted_text
    count=n
    temp=""
    res=encrypted_text
    while count>0:
        for i in range(0,len(encrypted_text)//2):
            temp+=encrypted_text[i+len(encrypted_text)//2:i+1+len(encrypted_text)//2]
            temp+=encrypted_text[i:i+1]
        encrypted_text=temp
        temp=""
        count-=1
    return encrypted_text if len(res)%2==0 else encrypted_text+res[-1]
def encrypt(text, n):
    count=0
    temp=""
    while count<n:
        for i in range(0,len(text)):
            if i%2==1:
                temp+=text[i:i+1]
        for i in range(0,len(text)):
            if i%2==0:
                temp+=text[i:i+1]
        text=temp
        temp=""
        count+=1
    return text