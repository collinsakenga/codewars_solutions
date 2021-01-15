def rankings(arr):
    dict={i:"" for i in arr}
    for i,j in enumerate(sorted(arr, reverse=True)):
        dict[j]=i+1
    return [i for i in dict.values()]