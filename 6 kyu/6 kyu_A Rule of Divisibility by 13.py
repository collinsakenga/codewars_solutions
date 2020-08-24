def thirt(n):
    pattern = [1, 10, 9, 12, 3, 4]
    compare = n
    index = 0
    temp = 0
    while True:
        for i in str(compare)[::-1]:
            temp += int(i)*pattern[index % 6]
            index += 1
        index = 0
        if temp == compare:
            return temp
        compare = temp
        temp = 0
