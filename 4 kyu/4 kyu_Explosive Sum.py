from bs4 import BeautifulSoup
import requests
res=requests.get("http://www.numericana.com/data/partition.htm")
dict={}
soup = BeautifulSoup(res.content, 'html.parser')
for i in soup.findAll("pre"):
    for j,k in enumerate(i.text.splitlines()):
        if j<=1:
            continue
        temp=k.strip().split(": ")
        dict[int(temp[0])]=int(temp[1])
def exp_sum(n):
    return dict[n]