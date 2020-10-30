def reduce_by_rules(lst, rules):
    res = lst.copy()
    for i in range(len(res)-1):
        res[i+1] = rules[i % len(rules)](res[i], res[i+1])
    return res[-1]