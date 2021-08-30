def make_a_window(num): 
    window=["|"+"."*num+"|"+"."*num+"|" for i in range(num)]
    return "\n".join(["-"*(3+2*num)]+window+["|"+"-"*num+"+"+"-"*num+"|"]+window+["-"*(3+2*num)])