numbers=[0, 1, 153, 370, 371, 407]
def is_sum_of_cubes(s):
    res=[]
    temp=""
    for i in s:
        if i.isdigit():
            temp+=i
        else:
            res.extend([temp[i:i+3] for i in range(0, len(temp), 3) if int(temp[i:i+3]) in numbers])
            temp=""
    res.extend([temp[i:i+3] for i in range(0, len(temp), 3) if int(temp[i:i+3]) in numbers])
    return " ".join(res)+f" {sum(int(i) for i in res)} Lucky" if res else "Unlucky"