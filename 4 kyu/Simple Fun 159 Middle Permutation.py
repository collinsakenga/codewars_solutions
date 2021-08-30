def middle_permutation(string):
    string="".join(sorted(string))
    res=""
    if len(string)%2==0:
        res+=string[len(string)//2-1]+string[len(string)-1]
        string=string[0:len(string)//2-1]+string[len(string)//2:len(string)-1]
    elif len(string)%2==1:
        res+=string[len(string)//2]+string[len(string)//2-1]
        string=string[0:len(string)//2-1]+string[len(string)//2+1:]
    return res+string[::-1]