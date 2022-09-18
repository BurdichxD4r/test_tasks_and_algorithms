from bs4 import BeautifulSoup
from requests import get
import time
import random


def limits(start, stop, user_number):
    if start <= user_number <= stop:
        return user_number
    else:
        print('[ERROR] Введенно некорректное значение!\n\tПовторите попытку!')
        return 0


def connecting_to_the_page(url_page):
    print('\n\n\n\n' + '\033[1m' + 'Сколько страниц просмотреть?' + '\033[0m', 'от 1 до 20')

    how_many_pages_to_view = limits(1, 20, int(input()))
    count = 1
    performances = []

    __info = "[INFO] На данной странице, нет ни одного доступного спектакля"
    __error = '[ERROR] Некорректно введена ссылка на страницу!'

    print('Loading ...')

    while count <= how_many_pages_to_view:
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
    parsing(performances)

def parsing(performances):

    count = 0
    name_data = []
    price_data = []
    date_data = []

    while len(performances) != 0:
        print('\n\n\n\n' + '\033[1m' + f'Сколько выступлений показать?' + '\033[0m', f'от 1 до {len(performances)}')
        how_many_performances_to_show = limits(0, len(performances), int(input()))
        if how_many_performances_to_show == 0:
            continue
        while count < how_many_performances_to_show:
            info = performances[count]
            name = info.find('h2').text
            name_data.append(name)
            price = info.find('span', {"data-testid": "event-card-price"}).find('span').find('span').text
            price_data.append(price)
            date = info.find('ul').find('li').text
            date_data.append(date)
            count += 1
        break
    demonstration(name_data, price_data, date_data)

def demonstration(name_data, price_data, date_data):
    if len(name_data) != 0:
        for n in range(len(name_data)):
            print(name_data[n], price_data[n], date_data[n])
