def limits(start, stop, user_number):
    if start <= user_number <= stop:
        return user_number
    else:
        print('[ERROR] Введенно некорректное значение!\n\tПовторите попытку!')
        return 0