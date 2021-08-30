import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
def wikiscraping(url):
    html=requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    lists = soup.find('div', attrs={'id':'bodyContent'})
    l2=lists.findAll(href=True)
    res={}
    for i in l2:
        if i["href"].startswith("/wiki") and ":" not in i["href"]:
            s=unquote(i["href"][6:].replace("_", " "))
            index=next((j for j,k in enumerate(s) if k=="#"), len(s))
            res[s[:index]]="https://en.wikipedia.org"+i["href"]
    return res