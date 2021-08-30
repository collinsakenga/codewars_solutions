def find_ball(scales):
    leftPan = [0,1,2,3]
    rightPan = [4,5,6,7]
    w = scales.get_weight(leftPan, rightPan)
    res=leftPan.copy() if w==-1 else rightPan.copy()
    leftPan=res[:2]
    rightPan=res[2:]
    w = scales.get_weight(leftPan, rightPan)
    res=leftPan.copy() if w==-1 else rightPan.copy()
    leftPan=res[:1]
    rightPan=res[1:]
    w = scales.get_weight(leftPan, rightPan)
    return res[0] if w==-1 else res[1]