def max_pizza(cut):
    return cut*(cut+1)//2+1 if cut >= 0 else -1
