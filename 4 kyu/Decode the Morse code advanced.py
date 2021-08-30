def decode_bits(bits):
    bits=bits.strip("0")
    low=len(bits)
    count=0
    zero=0
    count2=0
    for i in bits:
        if i=="1":
            count+=1
            zero=max(zero, count2)
            count2=0
        elif i=="0":
            if count: low=min(count, low)
            count=0
            count2+=1
    if zero:
        if low//zero==3: low//=3
    if count: low=min(count, low)
    res=bits.split("0"*low*7)
    string=""
    for i in res:
        index=0
        count1=0
        count0=0
        while index<len(i):
            if i[index]=="1":
                count1+=1
                if count0==low*3:
                    string+=" "
                count0=0
            elif i[index]=="0":
                count0+=1
                if count1>0 and count1!=low and count1<low*3:
                    string+="."
                elif count1==low:
                    string+="."
                elif count1==low*3:
                    string+="-"
                count1=0
            index+=1
        if count1>0 and count1!=low and count1<low*3:
            string+="."
        elif count1==low:
            string+="."
        elif count1==low*3:
            string+="-"
        string+="   "
    return string.rstrip()
def decode_morse(morseCode):
    string=[]
    res=morseCode.split("   ")
    for i in res:
        temp=""
        for j in i.split():
            temp+=MORSE_CODE[j]
        string.append(temp)
    return " ".join(string).lstrip()