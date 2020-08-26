def convert(input, source, target):
    num = 0
    index = 0
    for i in range(len(input)-1, -1, -1):
        num += source.index(input[index])*(len(source)**i)
        index += 1
    if num == 0:
        return target[0]
    index_target = 0
    while num >= len(target)**index_target:
        index_target += 1
    res = ""
    while index_target > 0:
        temp = num//(len(target)**(index_target-1))
        res += target[temp]
        num -= temp*(len(target)**(index_target-1))
        index_target -= 1
    return res
