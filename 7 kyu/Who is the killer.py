def killer(suspect_info, dead):
    for i,j in suspect_info.items():    
        flag=False
        for k in dead:
            if k not in j:
                flag=True
                break
        if not flag:
            return i