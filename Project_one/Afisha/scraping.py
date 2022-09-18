from bs4 import BeautifulSoup
from requests import get
import time
import random

def connecting_to_the_page(url_page):

    count = 1
    performances = []

    __info = "[INFO] На данной странице, нет ни одного доступного спектакля"
    __error = '[ERROR] Некорректно введена ссылка на страницу!'

    print('Loading ...')

    while count <= 1:
        print(f'Проверка страницы №{count}')
        url = url_page + '?page=' + str(count)
        html_soup = BeautifulSoup(get(url).text, 'html.parser')
        check = html_soup.find_all('div', class_="page-content")

        if len(check) == 0:
            print(__error)
            break

        performances_data = html_soup.find_all('div', class_="event events-list__item yandex-sans")
        if len(performances_data) != 0:
            performances.extend(performances_data)
            time.sleep(random.randint(1, 3) * 1.1)
        else:
            print(__info)
            break
        count += 1
    print('')
    parsing(performances)

def parsing(performances):

    count = 0
    name_data = []
    price_data = []
    date_data = []

    while count <= 5:
        info = performances[count]
        name = info.find('h2').text
        name_data.append(name)
        price = info.find('span', {"data-testid": "event-card-price"}).find('span').find('span').text
        price_data.append(price)
        date = info.find('ul').find('li').text
        date_data.append(date)
        count += 1
    demonstration(name_data, price_data, date_data)

def demonstration(name_data, price_data, date_data):
    for n in range(len(name_data)):
        print(name_data[n], price_data[n], date_data[n])
