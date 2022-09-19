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

def get_key(dict, value_user):
    for key, value in dict.items():
        if value == value_user:
            return key


performances_dict = {
    1: 'https://afisha.yandex.ru/saint-petersburg/selections/concert-hot',
    2: 'https://afisha.yandex.ru/saint-petersburg/selections/standup',
    3: 'https://afisha.yandex.ru/saint-petersburg/selections/concert-pop',
    4: 'https://afisha.yandex.ru/saint-petersburg/selections/highrated-plays',
    5: 'https://afisha.yandex.ru/saint-petersburg/selections/famous-actors',
    6: 'https://afisha.yandex.ru/saint-petersburg/selections/theatre-musical'
}