def hofstadter_Q(n):
    list = [1, 1]
    for i in range(2, n):
        list.append(list[i-list[i-1]]+list[i-list[i-2]])
    return list[n-1]