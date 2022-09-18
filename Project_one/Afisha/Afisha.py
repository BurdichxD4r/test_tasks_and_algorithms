from bs4 import BeautifulSoup
from requests import get
import time
import random




count = 0
performances = []
name_data = []
price_data = []
date_data = []


def url_page():
    print('''
    Какую категорию выбирите:
    1. Самые ожидаемые концерты
    2. Стендап
    3. Концерты популярной музыки
    4. Спектакли с высоким рейтингом
    5. Спектакли с известными актёрами
    6. Мюзиклы
    7. Выход из приложения
    ''')
    performances_dict = {
        1: 'https://afisha.yandex.ru/saint-petersburg/selections/concert-hot',
        2: 'https://afisha.yandex.ru/saint-petersburg/selections/standup',
        3: 'https://afisha.yandex.ru/saint-petersburg/selections/concert-pop',
        4: 'https://afisha.yandex.ru/saint-petersburg/selections/highrated-plays',
        5: 'https://afisha.yandex.ru/saint-petersburg/selections/famous-actors',
        6: 'https://afisha.yandex.ru/saint-petersburg/selections/theatre-musical'
    }
    while True:
        user_number = int(input())
        if 0 < user_number <= 6:
            connecting_to_the_page(performances_dict[user_number])
            break
        elif user_number == 7:
            break
        else:
            print('[Error] Введенно некорректное значение!\n\tПовторите попытку!')



def connecting_to_the_page(url_page):
    count = 1
    __info = "[INFO] На данной странице, нет ни одного доступного спектакля"
    __error = '[ERROR] Некорректно введена ссылка на страницу!'
    while count <= 1:
        url = url_page + '?page=' + str(count)
        html_soup = BeautifulSoup(get(url).text, 'html.parser')
        check = html_soup.find_all('div', class_="page-content")
        if len(check) == 0:
            print(__error)
            break
        performances_data = html_soup.find_all('div', class_="event events-list__item yandex-sans")
        if len(performances_data) != 0:
            performances.extend(performances_data)
            time.sleep(random.randint(1, 3) * 1.5)
        else:
            print(__info)
            break
        count += 1

url_page()

# while count <= 5:
#     info = performances[count]
#     name = info.find('h2').text
#     name_data.append(name)
#     price = info.find('span', {"data-testid": "event-card-price"}).find('span').find('span').text
#     price_data.append(price)
#     date = info.find('ul').find('li').text
#     date_data.append(date)
#     count += 1
#
# def demonstration():
#     for n in range(len(name_data)):
#         print(name_data[n], price_data[n], date_data[n])
#
# demonstration()