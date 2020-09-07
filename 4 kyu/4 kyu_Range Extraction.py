def solution(raw):
    result = []
    index = 0
    while index < len(raw):
        if (index+2) < len(raw) and raw[index+2]-raw[index+1] == raw[index+1]-raw[index] == 1:
            rec = raw[index]
            index += 2
            while index < len(raw) and raw[index]-raw[index-1] == 1:
                index += 1
            index -= 1
            result.append(f"{rec}-{raw[index]}")
        else:
            result.append(str(raw[index]))
        index += 1
    return ",".join(result)
