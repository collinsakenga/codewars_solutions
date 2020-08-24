def stat(strg):
    if not strg:
        return ""
    time = []
    temp = strg.split(", ")
    for i in temp:
        temp2 = i.split("|")
        time.append(int(temp2[0])*3600+int(temp2[1])*60+int(temp2[2]))
    time.sort()
    range = [(max(time)-min(time))//3600, (max(time)-min(time))//60 %
             60, (max(time)-min(time)) % 60]
    average = [sum(time)//len(time)//3600, sum(time) //
               len(time)//60 % 60, sum(time)//len(time) % 60]
    if len(time) % 2 == 0:
        median = [(time[len(time)//2]+time[len(time)//2-1])//2//3600, (time[len(time)//2] +
                                                                       time[len(time)//2-1])//2//60 % 60, (time[len(time)//2]+time[len(time)//2-1])//2 % 60]
    else:
        median = [time[len(time)//2]//3600, time[len(time)//2] //
                  60 % 60, time[len(time)//2] % 60]
    return "Range: "+"|".join(add_zero(range))+" Average: "+"|".join(add_zero(average))+" Median: "+"|".join(add_zero(median))


def add_zero(list):
    for i in range(0, len(list)):
        list[i] = str(list[i])
        if int(list[i]) < 10:
            list[i] = "0"+list[i]
    return list
