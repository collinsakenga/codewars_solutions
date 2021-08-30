def longest_repetition(chars):
    if not chars:
        return ('', 0)
    index=0
    count=1
    comp=1
    rec=chars[0]
    while index<len(chars)-1:
        if chars[index+1]==chars[index]:
            while index<len(chars)-1:
                if chars[index+1]!=chars[index]:
                    break
                comp+=1
                index+=1
        index+=1
        if comp>count:
            rec=chars[index-1]
            count=comp
        comp=1  
    return (rec, count)  