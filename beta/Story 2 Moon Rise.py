def formatter(curr_time, moon_rise, elapse_time):
    cur=minute(curr_time)
    after=minute(moon_rise)
    res=[curr_time]
    increment=int(elapse_time)
    for i in range(cur+increment, after+increment, increment):
        diff=after-i
        if diff<0:
            res.append('Past Moon Rise!')
        elif diff==0:
            res.append('Moon Rise!')
        elif diff==15:
            res.append('Quarter to Moon Rise!')
        elif diff==30:
            res.append('Half an hour until Moon Rise!')
        else:
            res.append(clock(i))
    return res
def minute(s):
    return int(s.split(":")[0])*60+int(s.split(":")[1])
def clock(n):
    return f"{n//60:02d}:{n%60:02d}"