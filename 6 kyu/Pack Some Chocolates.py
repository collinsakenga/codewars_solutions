# return the number of small chocolates required to achieve 
# the desired goal. Return -1 if the goal cannot be achieved 
def make_chocolates(small, big, goal):
    if small*2+big*5<goal:
        return -1
    res=min(big, goal//5)
    for i in range(res, max(res-2, -1), -1):
        check=divmod(goal-i*5, 2)
        if check[1]==0 and check[0]<=small:
            return check[0]
    return -1
