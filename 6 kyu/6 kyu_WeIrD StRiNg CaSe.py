def to_weird_case(string):
    string=string.split()
    result=""
    count=0
    for word in string:
        for char in word:
            if char.islower() and count%2==0:
                result+=char.upper()
            else:
                result+=char
            count+=1
        result+=" "
        count=0
    return result[:-1]