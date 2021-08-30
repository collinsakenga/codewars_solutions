def what_is_the_time(time):
    temp=translate(time) if translate(time) >0 else 720+translate(time)
    hr="{:02d}".format(temp//60)
    min="{:02d}".format(temp%60)
    return f"{hr}:{min}" if hr!="00" else f"12:{min}"
def translate(time):
    res=time.split(":")
    return 12*60-int(res[0])*60-int(res[1])