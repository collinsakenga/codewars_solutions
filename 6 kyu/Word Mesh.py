def word_mesh(arr):
    word=""
    for i in range(len(arr)-1):
        index=1
        comp=min(len(arr[i]), len(arr[i+1]))
        check=""
        while index<=comp:            
            if arr[i][len(arr[i])-index:]==arr[i+1][0:index]:
                check=arr[i+1][0:index]
            index+=1
        if not check:
            return "failed to mesh"
        word+=check
        index+=1
    return word