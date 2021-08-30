from bs4 import BeautifulSoup
import requests
def get_leaderboard_honor():
    url=requests.get("https://www.codewars.com/users/leaderboard")
    soup=BeautifulSoup(url.content, "html.parser")
    res=soup.find("div", {"class": "leaderboard p-0"})
    rank=[]
    for i,j in enumerate(res.table.findAll("tr")):
        temp=[k.text for k in j.findAll("td")]
        if not temp:
            continue
        rank.append(int(temp[-1].replace(",", "")))
    return rank
