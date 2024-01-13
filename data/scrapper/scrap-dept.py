from bs4 import BeautifulSoup
import requests
import pandas as pd

data = {
    'dept': [],
    'overview': [],
}

depts = ['bme', 'che', 'cse', 'eee', 'ipe', 'pme', 'te']

for dept in depts:
    URL = f"https://{dept}.just.edu.bd/about/overview"

    r = requests.get(URL)
    print('recieving signal:  ', r, URL)

    soup = BeautifulSoup(r.content, 'html5lib')

    p = soup.find('div', attrs = {'class': 'msg paragraph'}).text
    p = p.split(".")[0:8]
    p = ".".join(p)
    p += "."
    overview = p

    data['dept'].append(dept)
    data['overview'].append(overview)

    df = pd.DataFrame(data)
    df.to_csv('dept-overview.csv')