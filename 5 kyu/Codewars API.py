from bs4 import BeautifulSoup
import requests
import json
def all_links():
    url=requests.get("https://www.codewars.com/users/leaderboard")
    soup=BeautifulSoup(url.content, "html.parser")
    data=soup.find("div", {"class": "leaderboard p-0"})
    links=[]
    for i in data.findAll('a', href=True):
        links.append("https://www.codewars.com/api/v1"+i["href"])
    return links
links=all_links()
def get_codeChallenges(n):
    url=requests.get(links[n-1]) 
    soup=BeautifulSoup(url.content, "html.parser")
    data=json.loads(soup.text)
    return [data["codeChallenges"]['totalAuthored'], data["codeChallenges"]['totalCompleted']]