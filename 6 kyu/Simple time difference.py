def solve(arr):
    if len(arr)==1: return "23:59"
    arr=sorted(arr, key=lambda x: (int(x.split(":")[0]), int(x.split(":")[1])))
    rec=(int(arr[0].split(":")[0])+24-int(arr[-1].split(":")[0]))*60+int(arr[0].split(":")[1])-int(arr[-1].split(":")[1])-1
    for i in range(1,len(arr)):
        compare=(int(arr[i].split(":")[0])-int(arr[i-1].split(":")[0]))*60+int(arr[i].split(":")[1])-int(arr[i-1].split(":")[1])-1
        rec=max(compare, rec)
    return f"{'0'*(2-len(str(rec//60)))}{rec//60}:{'0'*(2-len(str(rec%60)))}{rec%60}"