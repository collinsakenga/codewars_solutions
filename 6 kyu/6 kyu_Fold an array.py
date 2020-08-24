def fold_array(array, runs):
    temp = []
    count = 0
    index = 0
    index2 = len(array)-1
    while runs > count:
        while index2 > index:
            temp.append(array[index]+array[index2])
            index += 1
            index2 -= 1
        if index2 == index:
            temp.append(array[index2])
        array = temp
        temp = []
        index = 0
        index2 = len(array)-1
        count += 1
    return array
