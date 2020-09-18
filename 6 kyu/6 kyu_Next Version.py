def next_version(version):
    res = [int(i) for i in version.split(".")]
    res[-1] += 1
    for i in range(len(res)-1, -1, -1):
        if i != 0 and res[i] == 10:
            res[i] = 0
            res[i-1] += 1
    return ".".join(str(i) for i in res)
