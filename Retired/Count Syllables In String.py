def count_syllables(word):
    total=0
    temp=""
    for i,j in enumerate(word+" "):
        if j in "aeiouy":
            temp+=j
        else:
            if not temp:
                continue
            total+=1
            temp=""
    return max(1, total-int(word[-1]=="e"))