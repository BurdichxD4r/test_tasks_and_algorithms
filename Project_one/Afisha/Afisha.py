from bs4 import BeautifulSoup
from requests import get
import time
import random

def scraping_menu():
    '''
    Основное меню осуществляющее навигацию в приложении
    '''

    print('\033[1m' + 'Меню навигации:' + '\033[0m' + '''
  1. Выбор категории
  2. Выход
''')

    pattern_menu(1, 2, dict=scraping_menu_dict)


def pattern_menu(start=1, stop=1, dict=None):
    '''
    Функция отвечающая за навигацию

    :param start: Начальный выбор в меню (всегда 1)
    :param stop: Последний пункт меню
    :param dict: Словарь с пунктами
    '''

    while True:
        user_number = int(input())
        if start <= user_number <= stop and type(dict[user_number]) == type(pattern_menu):
            dict[user_number]()
        elif start <= user_number <= stop:
            connecting_to_the_page(dict[user_number])
            time.sleep(5)
            exit_to_the_menu()
        else:
            print('[Error] Введенно некорректное значение!\n\tПовторите попытку!')


def url_page():

    print('''
Какую категорию выбирите:
  1. Самые ожидаемые концерты
  2. Стендап
  3. Концерты популярной музыки
  4. Спектакли с высоким рейтингом
  5. Спектакли с известными актёрами
  6. Мюзиклы
  7. В главное меню
    ''')

    pattern_menu(1, 7, performances_dict)


def exit_to_the_menu():
    print('\n\n\n\n' + '\033[1m' + 'Что дальше?' + '\033[0m' + '''
  1. В главное меню
  2. Выбор категорий
  3. Выход
''')

    pattern_menu(1, 3, dict=exit_to_the_menu_dict)


def exit_():
    print('Всего хорошего!')
    exit()


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


scraping_menu_dict = {
    1: url_page,
    2: exit_
}

performances_dict = {
    1: 'https://afisha.yandex.ru/saint-petersburg/selections/concert-hot',
    2: 'https://afisha.yandex.ru/saint-petersburg/selections/standup',
    3: 'https://afisha.yandex.ru/saint-petersburg/selections/concert-pop',
    4: 'https://afisha.yandex.ru/saint-petersburg/selections/highrated-plays',
    5: 'https://afisha.yandex.ru/saint-petersburg/selections/famous-actors',
    6: 'https://afisha.yandex.ru/saint-petersburg/selections/theatre-musical',
    7: scraping_menu
}

exit_to_the_menu_dict = {
        1: scraping_menu,
        2: url_page,
        3: exit_
    }


scraping_menu()