from bs4 import BeautifulSoup
import requests, json
sorting={'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, "beta":9}
def sort_by_rank(list_of_kata):
    res={}
    for i in list_of_kata:
        url=requests.get("https://www.codewars.com/api/v1/code-challenges/"+i)
        soup=BeautifulSoup(url.content, "html.parser")
        data=json.loads(soup.text)
        if data["rank"]["name"]=="null":
            res[i]="beta"
        else:
            res[i]=data["rank"]["name"].split()[0] 
    return [i[0] for i in sorted(res.items(), key=lambda x: (-sorting[x[1]], x[0]))]