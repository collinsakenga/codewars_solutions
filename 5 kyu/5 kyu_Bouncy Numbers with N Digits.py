from bs4 import BeautifulSoup
import requests
def memo():
    html=requests.get('https://oeis.org/A204692/b204692.txt')
    soup = BeautifulSoup(html.content, 'html.parser')
    return {i.split()[0]:i.split()[1] for i in soup.text.splitlines() if i}
res=memo()
def bouncy_count(number): 
    return int(res.get(str(number), 0))