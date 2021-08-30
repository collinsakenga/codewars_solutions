from itertools import product
dict={}
dict2={}
short=["".join(i) for _ in range(4) for i in product("abcdefghijklmnopqrstuvwxyz", repeat=_+1)]
index=0
def url_shortener(long_url):
    global index
    if not dict.get(long_url, None):
            dict[long_url]="short.ly/"+short[index]
            dict2["short.ly/"+short[index]]=long_url
            index+=1
    return dict[long_url]

def url_redirector(short_url):
    return dict2.get(short_url, "")