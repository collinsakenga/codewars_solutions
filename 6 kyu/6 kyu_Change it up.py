def changer(string):
    res=""
    for i in string:
        if not i.isalpha():
            res+=i
        else:
            temp="a" if i=="z" else "A" if i=="Z" else chr(ord(i)+1)
            res+=temp.upper() if temp in "aeiouAEIOU" else temp.lower()
    return res