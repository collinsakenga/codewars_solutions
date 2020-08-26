def encode_rail_fence_cipher(string, n):
    res = [[] for i in range(n)]
    index = 0
    index_n = 0
    flag = True
    while index < len(string):
        res[index_n].append(string[index])
        index += 1
        index_n += 1 if flag else -1
        if index_n == n-1:
            flag = False
        elif index_n == 0 and not flag:
            flag = True
    return "".join([j for i in res for j in i])


def decode_rail_fence_cipher(string, n):
    solution_index = 0
    res = [""]*len(string)
    step = (n-1)*2
    diff = (n-1)*2
    string_index = 0
    while solution_index < n:
        flag = True
        total = 0
        while total+solution_index < len(string):
            res[total+solution_index] = string[string_index]
            if solution_index == 0 or solution_index == n-1:
                total += step
            else:
                total += diff if flag else step-diff
                flag = not flag
            string_index += 1
        solution_index += 1
        diff -= 2
    return "".join(res)
