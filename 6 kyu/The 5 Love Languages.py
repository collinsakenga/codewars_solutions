def love_language(partner, weeks):
    count=0
    dict={}
    for i in LOVE_LANGUAGES:
        dict[i]=0
    index=0
    while count<weeks*7 or index<5:
        dict[LOVE_LANGUAGES[index]]+=1 if partner.response(LOVE_LANGUAGES[index])=="positive" else -1
        if dict[LOVE_LANGUAGES[index]]>3:
            return LOVE_LANGUAGES[index]
        elif dict[LOVE_LANGUAGES[index]]<-3:
            index+=1
        count+=1