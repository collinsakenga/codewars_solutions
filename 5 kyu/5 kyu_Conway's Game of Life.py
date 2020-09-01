from copy import deepcopy


def next_gen(cells):
    temp = deepcopy(cells)
    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            count = 0
            times = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if k < 0 or l < 0 or k >= len(cells) or l >= len(cells[i]) or (k == i and l == j):
                        continue
                    if temp[k][l] == 1:
                        count += 1
                    times += 1
            if temp[i][j] == 1 and (count < 2 or count > 3):
                cells[i][j] = 0
            elif temp[i][j] == 0 and count == 3:
                cells[i][j] = 1
    return cells
