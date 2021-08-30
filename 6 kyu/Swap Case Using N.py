def swap(s,n):
    res=bin(n)[2:]*(len(s)//len(bin(n)[2:])+1)
    index=0
    string=""
    for i in range(len(s)):
        if not s[i].isalpha(): 
            string+=s[i]
            continue
        string+=s[i].swapcase() if res[index]=="1" else s[i]
        index+=1
    return string
            
            