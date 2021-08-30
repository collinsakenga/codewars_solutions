def trump_detector(trump_speech):
    count=total=0
    trump_speech=trump_speech.lower()
    index=0
    while index<len(trump_speech):
        if trump_speech[index] in "aeiou":
            count+=1
            temp=trump_speech[index]
            index+=1
            while index<len(trump_speech) and trump_speech[index]==temp:
                total+=1
                index+=1
        else:
            index+=1
    return round(total/count, 2)