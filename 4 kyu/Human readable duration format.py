def format_duration(seconds):
    if not seconds:
        return "now"
    time=[31536000,86400,3600,60,1]
    result=[0,0,0,0,0]
    temp=["year","day","hour","minute","second"]
    text=""
    while seconds!=0:
        while seconds>=time[0]:
            seconds-=time[0]
            result[0]+=1
        while seconds>=time[1]:
            seconds-=time[1]
            result[1]+=1
        while seconds>=time[2]:
            seconds-=time[2]
            result[2]+=1
        while seconds>=time[3]:
            seconds-=time[3]
            result[3]+=1
        while seconds>=time[4]:
            seconds-=time[4]
            result[4]+=1
    count=0
    for i in range(0,5):
        if result[i]:
            count+=1  
        if result[i]>1:
            temp[i]+="s"
    for i in range(0,5):
        if count==1:
            if result[i]>=1:
                text+=str(result[i])+" "+temp[i]+" "
                count-=1
        elif count==2:
            if result[i]>=1:
                text+=str(result[i])+" "+temp[i]+" and "
                count-=1
        elif count>2:
            if result[i]>=1:
                text+=str(result[i])+" "+temp[i]+", "
                count-=1
    return text[:-1]