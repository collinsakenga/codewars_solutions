def bowling_score(rolls):
    index=0
    count=0
    total=0
    while count<9:
        if rolls[index]==10:
            total+=10+rolls[index+1]+rolls[index+2]
            index+=1
        elif rolls[index]+rolls[index+1]==10:
            total+=10+rolls[index+2]
            index+=2
        else:
            total+=rolls[index]+rolls[index+1]
            index+=2
        count+=1
    return total+sum(rolls[index:])