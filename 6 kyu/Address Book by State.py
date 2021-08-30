locations={'AZ': 'Arizona',
'CA': 'California',
'ID': 'Idaho',
'IN': 'Indiana',
'MA': 'Massachusetts',
'OK': 'Oklahoma',
'PA': 'Pennsylvania',
'VA': 'Virginia'}
def by_state(str):
    dict={}
    res=""
    for i in str.split("\n"):
        temp=i.replace(",","").split()
        if not temp:
            continue
        if not dict.get(locations[temp[-1]], None):
            dict[locations[temp[-1]]]=[" ".join(temp[:-1]+[locations[temp[-1]]])]
        else:
            dict[locations[temp[-1]]].append(" ".join(temp[:-1]+[locations[temp[-1]]]))
    for k,v in sorted(dict.items(), key=lambda x:x[0]):
        res+=k+"\r\n..... "+"\r\n..... ".join(sorted(v))+"\r\n "
    return res[:-3]