def max_ball(v0):
    time=0.1
    height=0
    while True:
        if (v0*1000*time/3600 - 0.5*9.81*time*time)<height:
            return round(time*10)-1
        height=v0*1000*time/3600 - 0.5*9.81*time*time
        time+=0.1