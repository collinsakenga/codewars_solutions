def play_pass(s, n):
    temp=list(s)
    for i,j in enumerate(temp):
        if not j.isalnum():
            continue
        if j.isupper():
            temp[i]=chr(ord("A")+(ord(j)-ord("A")+n)%26)
            if i%2==1:
                temp[i]=temp[i].lower()
        elif j.islower():
            temp[i]=chr(ord("a")+(ord(j)-ord("a")+n)%26)
            if i%2==0:
                temp[i]=temp[i].upper()
        else:
            temp[i]=str(9-int(j))
    return "".join(temp)[::-1]