def break_caesar(message):
    message=message.replace("?","").replace("!","").replace(":","").replace(",","").replace(".","").lower()
    count=[0,0]
    for i in range(26):
        comp=0
        for word in message.split():
            if shift(word, i) in WORDS:
                comp+=1
        if comp>count[0]:
            count[0]=comp
            count[1]=i
    return count[1]
def shift(text, num):
    text=list(text)
    for i,j in enumerate(text):
        text[i]=chr(ord("a")+(ord(j)-ord("a")-num)%26)
    return "".join(text)