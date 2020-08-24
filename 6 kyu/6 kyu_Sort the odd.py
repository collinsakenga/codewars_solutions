def sort_array(source_array):
    result_odd=[]
    result_even=[]
    for num in source_array:
        if num%2==0:
            result_even.append(num)
        else:
            result_odd.append(num)
    result_odd.sort()
    index_even=0
    index_odd=0
    for index in range(len(source_array)):
        if source_array[index]%2==0:
            source_array[index]=result_even[index_even]
            index_even+=1
        else:
            source_array[index]=result_odd[index_odd]
            index_odd+=1
    return source_array