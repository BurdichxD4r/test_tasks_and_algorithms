from scraping import connecting_to_the_page, parsing, demonstration
import time
import random


def scraping_menu():
    '''
    Основное меню осуществляющее навигацию в приложении
    '''

    print('\n\n\n\n' + '\033[1m' + 'Меню навигации:' + '\033[0m' + '''
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
        if limits(start, stop, user_number) and hasattr(dict[user_number], '__call__'):
            dict[user_number]()
        elif limits(start, stop, user_number):
            connecting_to_the_page(dict[user_number])
            time.sleep(5)
            exit_to_the_menu()
        else:
            continue



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


def limits(start, stop, user_number):
    if start <= user_number <= stop:
        return user_number
    else:
        print('[Error] Введенно некорректное значение!\n\tПовторите попытку!')
        return False



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