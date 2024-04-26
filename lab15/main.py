from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests

url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D0%B0%D0%BC%D1%8B%D1%85_%D0%B2%D1%8B%D1%81%D0%BE%D0%BA%D0%B8%D1%85_%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9_%D0%B8_%D1%81%D0%BE%D0%BE%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9_%D0%BC%D0%B8%D1%80%D0%B0"
text = requests.get(url).text

soup = BeautifulSoup(text, 'html.parser')
tables = soup.find_all('table')
for elem in tables[1]:
    for row in elem:
        if not isinstance(row, str):
            for i, td in enumerate(row):
                if i in [1, 3, 7, 13, 15]:
                    print(td.text, end="; ")
                # if i in [5]:
                #     link = td.find('img')
                #     print(link.get('src'))
                if i in [9, 11]:
                    print([ch for ch in td.children][-1], end="; ")
                if i in [17]:
                    print(td.text[:td.text.find('[')])
                if i in [19]:
                    links = td.find_all('a', class_='external text')
                    for link in links:
                        l = urlparse(link.get('href'))
                        params = parse_qs(l.query)
                        print(params['params'][0], end="; ")
                        break
            print("\n")