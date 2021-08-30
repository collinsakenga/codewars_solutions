def in_array(array1, array2):
    result=[]
    for word_one in set(array1):
        for word_two in array2:
            if word_one in word_two:
                result.append(word_one)
                break
    result.sort()
    return result