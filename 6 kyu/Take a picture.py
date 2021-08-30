def sort_photos(pics):
    res=sorted(pics, key=lambda x: (int(x.split(".")[0]), abc(x.split(".")[1])))
    index=next(i for i,j in enumerate(res[-1][::-1]) if not j.isdigit())
    temp=res[-1][:-index]
    num=int(res[-1][-index:])+1
    return res[-5:]+[temp+str(num)]
def abc(s):
    index=next(i for i,j in enumerate(s[::-1]) if not j.isdigit())
    return int(s[-index:])