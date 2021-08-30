def get_generation(cells, generations):
    res = [x[:] for x in cells]
    for gen in range(generations):
        flag = expand_x(res) or expand_y(res)
        if flag:
            for i in range(len(res)):
                res[i] = [0]+res[i]+[0]
            res = [[0]*len(res[0])]+res+[[0]*len(res[0])]
        temp = [x[:] for x in res]
        for i in range(len(res)):
            for j in range(len(res[i])):
                count = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k < 0 or l < 0 or k >= len(res) or l >= len(res[0]) or (k == i and l == j):
                            continue
                        if temp[k][l] == 1:
                            count += 1
                if temp[i][j] == 1 and (count < 2 or count > 3):
                    res[i][j] = 0
                elif temp[i][j] == 0 and count == 3:
                    res[i][j] = 1
    pop_x(res, 0)
    pop_x(res, -1)
    pop_y(res, 0)
    pop_y(res, -1)
    return res


def expand_x(res):
    for i in range(len(res)):
        if res[i][0] == 1 or res[i][-1] == 1:
            return True
    return False


def expand_y(res):
    for i in range(len(res[0])):
        if res[0][i] == 1 or res[-1][i] == 1:
            return True
    return False


def pop_x(res, index):
    for i in range(len(res)):
        if list(set(res[index])) == [0]:
            res.pop(index)
        else:
            break


def pop_y(res, index):
    flag = True
    for i in range(len(res[index])):
        for j in range(len(res)):
            if res[j][index] == 1:
                flag = False
                break
        if not flag:
            break
        for j in range(len(res)):
            res[j].pop(0) if index == 0 else res[j].pop()
