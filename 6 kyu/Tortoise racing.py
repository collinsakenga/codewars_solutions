from math import floor
def race(v1, v2, g):
    if v1>=v2:
        return None
    result=floor(3600*(g/(v2-v1)))
    hr,min,sec=0,0,0
    while result>0:
        if result>=3600:
            hr+=1
            result-=3600
        elif result>=60:
            min+=1
            result-=60
        elif result>=1:
            sec+=1
            result-=1
    return [hr,min,sec]