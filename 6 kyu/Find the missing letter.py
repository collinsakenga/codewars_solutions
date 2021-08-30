def find_missing_letter(testing):
    for char in range(len(testing)-1):
        if ord(testing[char+1])-ord(testing[char])>=2:
            return (chr(ord(testing[char])+1))
