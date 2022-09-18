from bs4 import BeautifulSoup
import requests
from requests import get
import time
import random

performances = []
page = 1
while page <= 1:
    url = 'https://afisha.yandex.ru/saint-petersburg/selections/spectacle?page=' + str(page)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    performances_data = html_soup.find_all('div', class_="event events-list__item yandex-sans")
    if performances_data != []:
        performances.extend(performances_data)
        time.sleep(random.randint(1, 3) * 1.5)
    else:
        print('empty')
        break
    page += 1

print(len(performances))
page = 0
while page <= 5:
    info = performances[page]
    price = info.find('span', {"data-testid": "event-card-price"}).find('span').find('span').text
    print(price)
    page += 1