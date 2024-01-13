import requests
from bs4 import BeautifulSoup
import pandas as pd

# demo data
data = {
    # 'uniqueid': [],
    'dept': [],
    'name': [],
    'designation': [],
    'extension': [],
    'telephone': [],
    'email': [],
    'researchgate': [],
    'linkedin': [],
    'facebook': [],
}

depts = [
    'bme', 'che', 'cse', 'eee', 'ipe', 'pme', 'te',
    'appt', 'cdm', 'est', 'nft',
    'fmb', 'gebt', 'mb', 'phm',
    'nhs', 'pes', 'ptr',
    'eng',
    'chem', 'mth', 'phy',
    'ais', 'fb', 'mgt', 'mkt'
]

for dept in depts:
    URL = f'https://{dept}.just.edu.bd/people/faculty'

    try:
        r = requests.get(URL)

        print()
        print('recieving signal:  ', r, URL)
        print()

        soup = BeautifulSoup(r.content, 'html5lib')
        peoples = soup.find_all('div', attrs = {'class': 'people'})

        for i, people in enumerate(peoples):
            # if i == 3:
            #     break
            name = designation = extension = None
            try:
                name = people.find('p', attrs = {'class': 'card-title'} )
                designation = people.find('p', attrs = {'class': 'card-paragraph italic mb-1'} )
                extension = people.find('read-more')['text']
            except TypeError as e:
                print(f"error: {e}")

            # print(name)
            # data['uniqueid'].append(i)
            data['dept'].append(dept)
            if name.text: data['name'].append(name.text)
            else: data['name'].append('Null')
            if designation.text: data['designation'].append(designation.text)
            else: data['designation'].append("Null")
            if extension: data['extension'].append(extension)
            else: data['extension'].append('Null')

            URL_PEOPLE = people.find('a')['href']
            GO_TO = "https://just.edu.bd" + URL_PEOPLE + "/contact"
            pr = requests.get(GO_TO)
            print('reading data:  ', pr, GO_TO)
            psoup = BeautifulSoup(pr.content, 'html5lib')

            try:
                contacts = psoup.find('div', attrs={'class': 'mt-4'}).find_all('a')
                # ['href']
                telephone = email = researchgate = linkedin = facebook = None
                for contact in contacts:
                    link = contact['href']
                    if 'tel' in link: telephone = link
                    elif '@' in link: email = link
                    elif 'researchgate' in link: researchgate = link
                    elif 'linkedin' in link: linkedin = link
                    elif 'facebook' in link: facebook = link

                if telephone: data['telephone'].append(telephone) 
                else: data['telephone'].append('Null')
                if email: data['email'].append(email) 
                else: data['email'].append('Null')
                if researchgate: data['researchgate'].append(researchgate) 
                else: data['researchgate'].append('Null')
                if linkedin: data['linkedin'].append(linkedin) 
                else: data['linkedin'].append('Null')
                if facebook: data['facebook'].append(facebook) 
                else: data['facebook'].append('Null')

            except AttributeError as e:
                print(f"no contact available: {e}")
                data['telephone'].append('Null')
                data['email'].append('Null')
                data['researchgate'].append('Null')
                data['linkedin'].append('Null')
                data['facebook'].append('Null')

            # print()
            # print(pd.DataFrame(data))
            df = pd.DataFrame(data)
            df.to_csv('data.csv')
            print('saved as data.csv')
            print()

    except TypeError as e:
        print(f'error: {e} at {dept}')







