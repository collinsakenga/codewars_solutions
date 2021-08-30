def gen():
    table={}
    count=0
    for k in "abcdefghijklmnopqrstuvwxyz":
        if k=="j" or k=="v":
            count+=1
        table[k]="{:05b}".format(ord(k)-ord("a")-count).replace("0", "a").replace("1", "b")
    return table
table=gen()
def baconian_cipher(text):
    return " ".join(table[i] for i in (j for j in text.lower() if j.isalpha()))
        
            