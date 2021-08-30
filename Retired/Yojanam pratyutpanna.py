def yojanam(arr,size):
    return helper(arr, True)
def helper(arr, flag):
    if len(arr)==1:
        return arr[0]
    if flag:
        return helper([arr[i]+arr[i+1] for i in range(0, len(arr), 2)], not flag)
    return helper([arr[i]*arr[i+1] for i in range(0, len(arr), 2)], not flag)