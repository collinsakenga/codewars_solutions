def fire_and_fury(tweet):
    for i in tweet:
        if i not in "EFIRUY":
            return 'Fake tweet.'
    res=[]
    count=0
    count2=0
    for i in range(len(tweet)-3):
        if tweet[i:i+4]=="FIRE":
            if count2:
                res.append(" ".join(["I", "am"]+["really"]*(count2-1)+["furious."]))
                count2=0
            count+=1
        elif tweet[i:i+4]=="FURY":
            if count:
                res.append(" ".join(["You"]+["and" ,"you"]*(count-1)+["are" ,"fired!"]))               
                count=0
            count2+=1
    if count2:       
        res.append(" ".join(["I", "am"]+["really"]*(count2-1)+["furious."]))
    if count:
        res.append(" ".join(["You"]+["and" ,"you"]*(count-1)+["are" ,"fired!"]))
    return 'Fake tweet.' if not res else " ".join(res)