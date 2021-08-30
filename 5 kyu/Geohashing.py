from hashlib import md5
import datetime
dict={j:i for i,j in enumerate("0123456789abcdef")}
def geohash(dow, date=datetime.datetime.now()):
    encode="-".join([str(date.year), f"{date.month:02d}", f"{date.day:02d}", f"{dow:.2f}"])
    res=md5(encode.encode('utf-8')).hexdigest()
    return [float(f"{hex_dec(res[i:i+len(res)//2]):.6f}") for i in range(0, len(res), len(res)//2)] 
def hex_dec(s):
    total=0
    start=16
    for i in s:
        total+=dict[i]/start
        start*=16
    return total