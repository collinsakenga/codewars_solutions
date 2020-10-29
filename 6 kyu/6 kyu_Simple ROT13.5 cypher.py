def ROT135(input):
    word={j:i for i,j in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    word2={j:i for i,j in word.items()}
    word3={j:i for i,j in enumerate("abcdefghijklmnopqrstuvwxyz")}
    word4={j:i for i,j in word3.items()}
    digit={j:i for i,j in enumerate("0123456789")}
    digit2={j:i for i,j in digit.items()}
    res=""
    for i in input:
        if i.isupper():
            res+=word2[(word[i]+13)%26]
        elif i.islower():
            res+=word4[(word3[i]+13)%26]
        elif i.isdigit():
            res+=digit2[(digit[i]+5)%10]
        else:
            res+=i
    return res