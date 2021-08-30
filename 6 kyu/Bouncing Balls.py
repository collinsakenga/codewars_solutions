def bouncing_ball(h, bounce, window):
    if not(h>0 and window<h and (bounce >0 and bounce <1)):
        return -1
    count=0
    while h>window:
        h*=bounce
        count+=1
    return count*2-1