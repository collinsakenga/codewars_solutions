from math import log
def squared_digits_series(n):
    power=log(n, 2)
    up=10
    down=1
    total=up+down
    for i in range(0, int(power)):
        down*=2
        up*=4
        total+=up+down
    return total-(2**int(power)-(n-down)-1)*(down*10+1)