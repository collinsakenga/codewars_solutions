def calculate_1RM(w, r):
    if r==0:
        return 0
    elif r==1:
        return w
    return round(max(w*r**0.1, w*(1+r/30), 100*w/(101.3-2.67123*r)))