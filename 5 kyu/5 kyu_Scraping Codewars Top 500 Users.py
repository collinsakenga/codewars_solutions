from bs4 import BeautifulSoup
import requests
URL = 'https://www.codewars.com/users/leaderboard'
class leaderboard():
    def __init__(self):
        self.position={}
    def set_dict(self, index, data):
        self.position[index]=data
class data:
    def __init__(self, name, clan, honor):
        self.name=name
        self.clan=clan
        self.honor=honor
def solution():
    res=requests.get(URL)
    soup=BeautifulSoup(res.content, 'html.parser')
    board=leaderboard()
    for j in soup.find_all("div", class_="leaderboard p-0"):
        for k,l in enumerate(j.table):
            if k==0:
                continue
            temp=list(l)
            person=data(l.attrs['data-username'], temp[2].text, int("".join(m for m in temp[3].text if m.isdigit())))
            board.set_dict(k, person)
    return board