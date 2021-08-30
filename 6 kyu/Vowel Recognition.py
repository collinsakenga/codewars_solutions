def vowel_recognition(s):
    total=0
    length=len(s)
    for i,j in enumerate(s):
        if j not in "aeiouAEIOU":
            continue
        total+=(length-i)*(i+1)
    return total
    