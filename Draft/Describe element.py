def describe_element(arr,num):
    count=arr.index(num)+1
    len_list=len(arr)
    if len_list%2==0:
        return "Left "+str(count) if count<=len_list/2 else "Right "+str(len_list-count+1)
    return "Left "+str(count) if count<(len_list//2)+1 else "Middle" if count==(len_list//2)+1 else "Right "+str(len_list-count+1)