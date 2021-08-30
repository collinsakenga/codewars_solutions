def order_breaker(array):
    res=next((j, array[i+1]) for i,j in enumerate(array[:-1]) if array[i+1]<j)
    temp=[i for i in array if i!=res[0]]
    return res[0] if sorted(temp)==temp else res[1]