def count_smileys(arr):
    total=0
    for i in arr:
        if i in ":):D;);D:-):-D;-);-D:~):~D;~);~D":
            total+=1
    return total