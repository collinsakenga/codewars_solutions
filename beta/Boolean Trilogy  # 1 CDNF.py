def cdnf(truth_table):
    res = []
    for i in truth_table:
        if i[-1] == 0:
            continue
        string = []
        for index, j in enumerate(i[:-1]):
            string.append(
                f"x{index+1}") if j == 1 else string.append(f"~x{index+1}")
        res.append("("+" * ".join(string)+")")
    return " + ".join(res)