def wave(people):
    temp = ""
    result = []
    for i in range(0, len(people)):
        if people[i].isalpha():
            temp += people[0:i]+people[i].upper()+people[i+1:]
            result.append(temp)
            temp = ""
    return result
