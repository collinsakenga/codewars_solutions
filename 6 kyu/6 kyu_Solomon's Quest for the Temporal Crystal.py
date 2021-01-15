def solomons_quest(array):
    location=[0,0]
    layer=0
    for arr in array:
        layer+=arr[0]
        if arr[1]==0:
            location[1]+=arr[2]*(2**layer)
        elif arr[1]==1:
            location[0]+=arr[2]*(2**layer)
        elif arr[1]==2:
            location[1]-=arr[2]*(2**layer)
        elif arr[1]==3:
            location[0]-=arr[2]*(2**layer)
    return location