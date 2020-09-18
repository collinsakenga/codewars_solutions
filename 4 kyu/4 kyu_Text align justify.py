def justify(text, width):
    rec = text.split()
    res = []
    space = 0
    record = 0
    index = 0
    length = 0
    while True:
        if index >= len(rec):
            temp = []
            for i in range(record, index):
                temp.append(rec[i])
            res.append(" ".join(temp))
            break
        space += 1
        length += len(rec[index])
        index += 1
        if (space+length-1) > width:
            index -= 1
            space -= 1
            length -= len(rec[index])
            if space != 1:
                temp = ""
                divide = width-length
                flag = True if divide % (space-1) == 0 else False
                max = divide//(space-1)+1 if divide % (space -
                                                       1) != 0 else divide//(space-1)
                space_count = []
                rec_max = max
                while (space-1) > 0:
                    space_count.append(max)
                    space -= 1
                    divide -= max
                    if not flag:
                        if rec_max == max and (space-1) > 0 and divide % (space-1) == 0:
                            max -= 1
                for i in range(record, index):
                    temp += rec[i]
                    try:
                        temp += " "*space_count[i-record]
                    except:
                        pass
                res.append(temp)
            else:
                res.append(rec[index-1])
            record = index
            space = 0
            length = 0
    return "\n".join(res)
