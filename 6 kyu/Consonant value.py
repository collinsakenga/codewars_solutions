def solve(s):
    index=0
    #replace vowels with " "
    for char in s:
        if char in "aeiou":
            s=s[:index]+" "+s[index+1:]
        index+=1
    total=0
    comp=0
    for word in s.split():
        #calculate word value
        for char in word:
            comp+=ord(char)-ord("a")+1        
        #get the max value
        if comp>total:
            total=comp
        #reset variable
        comp=0
    return total