def bubble(l):
    if not l:
        return []
    result = []
    for i in range(0, len(l)-1):
        for j in range(0, len(l)-1-i):
            if l[j] > l[j+1]:
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp
                result.extend(l)
    return [result[x*len(l):(x+1)*(len(l))] for x in range(0, len(result)//len(l))]
