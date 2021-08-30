def rgb(r, g, b):
    s=""
    if r>255:
        r=255
    elif g>255:
        g=255
    elif b>255:
        b=255
    if r<0:
        r=0
    elif g<0:
        g=0
    elif b<0:
        b=0
    r='{0:x}'.format(r)
    g='{0:x}'.format(g)
    b='{0:x}'.format(b)
    if int(r,16)<=15 and int(r,16)>=0:
        r='0'+r
    if int(g,16)<=15 and int(g,16)>=0:
        g='0'+g
    if int(b,16)<=15 and int(b,16)>=0:
        b='0'+b
    s+=r+g+b
    return s.upper()
