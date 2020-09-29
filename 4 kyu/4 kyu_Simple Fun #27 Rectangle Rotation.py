from math import sqrt


def rectangle_rotation(a, b):
    w1 = int((a/sqrt(2))//2)*2+1
    w2 = int(a/sqrt(2)/2+0.5)*2
    h1 = int((b/sqrt(2))//2)*2+1
    h2 = int(b/sqrt(2)/2+0.5)*2
    return w1*h1 + w2*h2
