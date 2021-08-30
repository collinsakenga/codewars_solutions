import requests
from bs4 import BeautifulSoup
def memo():
    url=requests.get("https://oeis.org/A004977/b004977.txt")
    soup=BeautifulSoup(url.content, "html.parser")
    table={}
    for i in soup.text.splitlines():
        number, total=i.split()
        table[int(number)]=int(total)
    return table
res=memo()
def look_and_say_and_sum(n):
    return res[n]