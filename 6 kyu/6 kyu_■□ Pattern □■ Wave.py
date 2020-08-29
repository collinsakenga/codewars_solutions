def draw(waves):
    res = [["□"]*len(waves) for i in range(max(waves))]
    for i in range(len(waves)):
        for j in range(max(waves)-1, max(waves)-1-waves[i], -1):
            res[j][i] = "■"
    return "\n".join(["".join(i) for i in res])
