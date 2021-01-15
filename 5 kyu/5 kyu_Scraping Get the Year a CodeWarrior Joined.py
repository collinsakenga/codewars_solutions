from bs4 import BeautifulSoup
import requests
def get_member_since(username):
    html=requests.get("https://www.codewars.com/users/"+username)
    soup = BeautifulSoup(html.content, 'html.parser')
    lists = soup.findAll('div', attrs={'class':'stat'})
    year=""
    for i in lists:
        temp=i.text.split(":")
        if temp[0]=='Member Since':
            year=temp[1]
            break
    return year