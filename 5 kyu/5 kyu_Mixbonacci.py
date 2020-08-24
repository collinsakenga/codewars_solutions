def mixbonacci(pattern, length):
    if not pattern or not length:
        return []
    dict = {'fib': 0, 'pad': 0, 'jac': 0, 'pel': 0, 'tri': 0, 'tet': 0}
    pattern_new = pattern*(length//len(pattern)+1)
    res = []
    for i in range(length):
        if pattern_new[i] == "fib":
            res.append(fib(dict["fib"]))
            dict["fib"] += 1
        elif pattern_new[i] == "pad":
            res.append(pad(dict["pad"]))
            dict["pad"] += 1
        elif pattern_new[i] == "jac":
            res.append(jac(dict["jac"]))
            dict["jac"] += 1
        elif pattern_new[i] == "pel":
            res.append(pel(dict["pel"]))
            dict["pel"] += 1
        elif pattern_new[i] == "tri":
            res.append(tri(dict["tri"]))
            dict["tri"] += 1
        elif pattern_new[i] == "tet":
            res.append(tet(dict["tet"]))
            dict["tet"] += 1
    return res


def fib(n, fib_list=[0, 1]):
    if len(fib_list) <= n:
        fib_list.append(fib(n-1)+fib(n-2))
    return fib_list[n]


def pel(n, pel_list=[0, 1]):
    if len(pel_list) <= n:
        pel_list.append(2*pel(n-1)+pel(n-2))
    return pel_list[n]


def pad(n, pad_list=[1, 0, 0]):
    if len(pad_list) <= n:
        pad_list.append(pad(n-2)+pad(n-3))
    return pad_list[n]


def jac(n, jac_list=[0, 1]):
    if len(jac_list) <= n:
        jac_list.append(jac(n-1)+2*jac(n-2))
    return jac_list[n]


def tri(n, tri_list=[0, 0, 1]):
    if len(tri_list) <= n:
        tri_list.append(tri(n-1)+tri(n-2)+tri(n-3))
    return tri_list[n]


def tet(n, tet_list=[0, 0, 0, 1]):
    if len(tet_list) <= n:
        tet_list.append(tet(n-1)+tet(n-2)+tet(n-3)+tet(n-4))
    return tet_list[n]
