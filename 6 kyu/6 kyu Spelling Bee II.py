def how_many_bees(hive):
    if not hive:
        return 0
    total=0
    for i in range(len(hive)):
        for j in range(len(hive[i])-2):
            comp="".join(hive[i][j:j+3])
            if comp=="bee" or comp=="eeb":
                total+=1
    for i in range(len(hive[0])):
        for j in range(len(hive)-2):
            comp=hive[j][i]+hive[j+1][i]+hive[j+2][i]
            if comp=="bee" or comp=="eeb":
                total+=1
    for i in range(len(hive)-2):
        for j in range(len(hive[i])-2):
            comp=hive[i][j]+hive[i+1][j+1]+hive[i+2][j+2]
            if comp=="bee" or comp=="eeb":
                total+=1
    for i in range(2, len(hive)):
        for j in range(len(hive[i])-2):
            comp=hive[i][j]+hive[i-1][j+1]+hive[i-2][j+2]
            if comp=="bee" or comp=="eeb":
                total+=1
    return total