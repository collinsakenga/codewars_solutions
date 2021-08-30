def solve(st):
    product=[]
    letter=[]
    temp2=temp=res=""
    for i in st:
        if i.isdigit():   
            temp+=i
        elif i=="(":
            product.append(int(temp or "1"))
            letter.append(temp2)
            temp2=temp=""
        elif i==")":   
            if temp2:
                letter.append(temp2)
                temp2=""
            count=product.pop()
            char=letter.pop()
            res=(char+res)*count
        else:
            temp2+=i
    return "".join(letter)+res