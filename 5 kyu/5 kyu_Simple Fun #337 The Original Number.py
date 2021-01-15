from collections import Counter
dict={'ZERO': 0, 'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9}
dict2={j:i for i,j in dict.items()}
def original_number(s):
    temp=Counter(s)
    res=""
    count=0
    if temp.get("U", None):
        check=temp["U"]
        res+="4"*check
        for i in "FOUR":
            temp[i]-=check
    if temp.get("X", None):
        check=temp["X"]
        res+="6"*check
        for i in "SIX":
            temp[i]-=check
    if temp.get("Z", None):
        check=temp["Z"]
        res+="0"*check
        for i in "ZERO":
            temp[i]-=check
    if temp.get("W", None):
        check=temp["W"]
        res+="2"*check
        for i in "TWO":
            temp[i]-=check
    if temp.get("R", None) and temp["R"]>0:
        check=temp["R"]
        res+="3"*check
        for i in "THREE":
            temp[i]-=check
    if temp.get("T", None) and temp["T"]>0:
        check=temp["T"]
        res+="8"*check
        for i in "EIGHT":
            temp[i]-=check
    if temp.get("O", None) and temp["O"]>0:
        check=temp["O"]
        res+="1"*check
        for i in "ONE":
            temp[i]-=check
    if temp.get("F", None) and temp["F"]>0:
        check=temp["F"]
        res+="5"*check
        for i in "FIVE":
            temp[i]-=check
    if temp.get("V", None) and temp["V"]>0:
        check=temp["V"]
        res+="7"*check
        for i in "SEVEN":
            temp[i]-=check
    if temp.get("I", None) and temp["I"]>0:
        check=temp["I"]
        res+="9"*check
        for i in "NINE":
            temp[i]-=check
    return "".join(sorted(res))