def reverse_and_combine_text(text):
    temp = text.split()
    while len(temp) > 1:
        res = []
        for i in range(0, len(temp), 2):
            try:
                res.append(temp[i][::-1]+temp[i+1][::-1])
            except:
                break
        if len(temp) % 2 == 1:
            res.append(temp[-1][::-1])
        temp = res.copy()
    return "".join(temp)
