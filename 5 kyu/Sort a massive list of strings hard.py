from heapq import *
def sort(words):
    res=[]
    for i in words:
        heappush(res, i)
    while res:
        yield heappop(res)