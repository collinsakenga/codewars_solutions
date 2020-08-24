def solution(s):
    if len(s) % 2 == 1:
        s += "_"
    result = []
    count = 0
    while True:
        if count+2 > len(s):
            break
        result.append(s[count:count+2])
        count += 2
    return result
