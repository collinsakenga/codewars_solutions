def find_part_max_prod(n):
    list=[2 for i in range(n//3+1)]
    if n%3==0:
        list.pop(0)
    for i in range(n-sum(list)):
        list[i]+=1
    total=1 
    for i in list:
        total*=i
    if n%3==1:
        list2=[3 for i in range(n//3)]
        list2[0]+=1
        return [list2, list, total]
    else:
        return [list, total]