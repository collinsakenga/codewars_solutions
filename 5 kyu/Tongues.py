def tongues(code):
    vowel='aiyeou'
    vowel2=vowel.upper()
    others="bkxznhdcwgpvjqtsrlmf"
    others2=others.upper()
    res=""
    for i in code:
        if i in vowel:
            res+=(vowel[(vowel.index(i)+3)%len(vowel)])
        elif i in vowel2:
            res+=(vowel2[(vowel2.index(i)+3)%len(vowel2)])
        elif i in others:
            res+=(others[(others.index(i)+10)%len(others)])
        elif i in others2:
            res+=(others2[(others2.index(i)+10)%len(others2)])
        else:
            res+=i
    return res
    