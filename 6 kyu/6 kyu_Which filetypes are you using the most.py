def solve(files):
    if not files:
        return []
    dict = {}
    for i in files:
        dict["."+i.split(".")[-1]] = dict.get("."+i.split(".")[-1], 0)+1
    res = {i: j for i, j in sorted(dict.items(), key=lambda x: (-x[1], x[0]))}
    check = set()
    most_common = []
    for i, j in res.items():
        check.add(j)
        if len(check) >= 2:
            return most_common
        most_common.append(i)
