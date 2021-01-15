from bs4 import BeautifulSoup
import requests
def memo():
    html=requests.get('https://oeis.org/A204692/b204692.txt')
    soup = BeautifulSoup(html.content, 'html.parser')
    return {i.split()[0]:i.split()[1] for i in soup.text.splitlines() if i}
res=memo()
def total_inc_dec(x):
    return 10**x-int(res.get(str(x), 0))