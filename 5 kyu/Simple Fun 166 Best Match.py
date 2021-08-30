def best_match(goals1, goals2):
    comp=max(goals1)
    comp2=0
    index=0
    for i in range(len(goals1)):
        diff=goals1[i]-goals2[i]
        if diff<comp or (diff==comp and comp2<goals2[i]):
            comp=min(comp, diff)
            comp2=goals2[i]
            index=i
    return index