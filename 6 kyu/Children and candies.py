from copy import deepcopy
def distribution_of_candy(candies):
    count=0
    while len(set(candies))>1:
        res=deepcopy(candies)
        for i in range(len(candies)):
            if candies[i]%2:
                res[i]+=1
                candies[i]+=1
            if i==len(candies)-1:
                res[0]+=candies[-1]//2
                res[-1]-=candies[-1]//2
            else:
                res[i+1]+=candies[i]//2
                res[i]-=candies[i]//2
        candies=deepcopy(res)
        count+=1
    return [count, candies[0]]