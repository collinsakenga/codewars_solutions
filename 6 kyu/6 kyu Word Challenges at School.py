def wanted_words(n, m, forbid_let):
    vowels={i:"" for i in "aeiou"}
    consonants={i:"" for i in "bcdfghjklmnpqrstvwxyz"}
    for i in forbid_let:
        if i in vowels:
            del vowels[i]
        elif i in consonants:
            del consonants[i]
    string_list=[]
    for i in WORD_LIST:
        flag=True
        for char in forbid_let:
            if char in i:
                flag=False
                break
        if not flag:
            continue
        res=[0,0]
        for char in i:
            if char in vowels:
                res[0]+=1
            elif char in consonants:
                res[1]+=1
        if res[0]==n and res[1]==m:
            string_list.append(i)
    return string_list