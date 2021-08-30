def root(number, exp):
    ans=round(number**(1/exp), 10)
    return ans if int(ans)==ans else None