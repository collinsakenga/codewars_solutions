def solve(n):
    if n < 10:
        return n
    else:
        append_string = ""
        temp = list(str(n))
        total = 0
        index = 0
        for num in temp:
            total += int(num)
        if total >= int(temp[0])+9*(len(temp)-1)-1:
            return n
        if int(temp[0]) != 9 and int(temp[1]) != 9:
            return int(str(int(temp[0])-1)+"9"*(len(temp)-1))
        else:
            for num in temp:
                if num != "9" and index > 0:
                    break
                append_string += num
                index += 1
            return int(str(int(append_string)-1)+"9"*(len(temp)-index))
