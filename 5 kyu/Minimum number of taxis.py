from heapq import *
def min_num_taxis(requests):
    res=[]
    for i,j in sorted(requests, key=lambda x: x[0]):
        if res and i>res[0]:
            heappop(res)
        heappush(res, j)   
    return len(res)