from colorama import Fore
import os
import json



# БАЗА
office_base = {}
with open('base.txt') as inp:
    for i in inp.readlines():
        key, val = i.strip().split(':')
        office_base[key] = val
films_base = {}  
temp = []
count = 0
with open('film_base.txt', 'r') as filehandle:
    for line in filehandle:
        print(temp)
        
        count += 1
        if count == 9:
            films_base[len(films_base) + 1] = temp
            currentPlace = line[:-1]
            temp.append(currentPlace)
            temp = []
            count = 0
        else:
            currentPlace = line[:-1]
            temp.append(currentPlace)
        
        
    for k, v in films_base.items():
        v[7] = int(v[7])
        v[8] = int(v[8])


# ФУНКЦИИ
def you_sure(choose_in_office):
    choose = input(Fore.YELLOW + 'Желаете продолжить ?\n(Да/Нет): ' + Fore.WHITE).lower()
    if choose == 'нет':
        main()
    elif choose == 'да':
        pass
    else:
        print(Fore.RED + 'Неизвестная команда, повторите ещё' + Fore.WHITE)


def film_add(films_base):
    while True:
        os.system('clear')
        value = []
        s = ''
        s = input('Введите название фильма: ').title()
        value.append(s)
        s = input('Введите кинотетр: ').title()
        value.append(s)
        s = input('Введите дату начала показа: ')
        value.append(s)
        s = input('Введите дату конца показа: ')
        value.append(s)
        s = input('Введите время показа: ')
        value.append(s)
        s = input('Введите возростное ограничение: ')
        value.append(s)
        while True:
            print(Fore.YELLOW + 'Выберите зал:\n1) | Большой\n2) | Малый' + Fore.WHITE)
            s = int(input('Номер: '))
            if s == 1:
                s = 'Большой'
                break
            elif s == 2:
                s = 'Малый'
                break
            else:
                continue
        value.append(s)
        while True:
            s = int(input('Введите количество обычных мест(10-120): '))
            if value[-1] == 'Большой' and (s <= 20 or s >= 120):
                print(Fore.RED + 'Данное количество мест неккоректно, повторите ещё' + Fore.WHITE)
                continue
            elif value[-1] == 'Малый' and (s <= 10 or s >= 60):
                print(Fore.RED + 'Данное количество мест неккоректно, повторите ещё' + Fore.WHITE)
                continue
            else:
                break
        value.append(s)
        while True:
            s = int(input('Введите количество комфортных мест: '))
            if value[-1] == 'Большой зал' and s <= 5 or s >= 30:
                print(Fore.RED + 'Данное количество мест неккоректно, повторите ещё' + Fore.WHITE)
                continue
            elif value[-1] == 'Малый зал' and s <= 2 or s >= 20:
                print(Fore.RED + 'Данное количество мест неккоректно, повторите ещё' + Fore.WHITE)
                continue
            else:
                break
        value.append(s)
        for k, v in films_base.items():
            if value[1] == v[1] and value[4] == v[4] and value[6] == v[6]:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            break
        else:
            print(Fore.RED + 'Введённые данные некорректны, выберите другой(Зал\\Кинотеатр\\Время)' + Fore.WHITE)
    print('HERE')
    return value


def add_account(office_base, login):
    p1 = input('Введите пароль: ')
    p2 = input('Повторите пароль: ')
    while p1 != p2:
        print(Fore.RED + 'Пароли не совпадают' + Fore.WHITE)
        p1 = input('Введите пароль заново: ')
        p2 = input('Повторите пароль: ')
    else:
        office_base[login] = p2


def print_ticket(theatre, start, end, free_seats, hall, time, price):  # итоговая печать билета
    os.system('clear')
    s = start[0:2] + theatre[0:2] + str(free_seats) + end[0:2]
    print('-' * 41,
          f'\n|\t\t\t\t\t|\n|\t\tБилет\t\t\t|\n|\tНомер билета: {s}\t\t|\n|\t{hall}\t\t\t|\n|\tВремя показа {time}\t\t|\n|\tЦена составит {price}\t\t|\n|\tОплата в кинотетре\t\t|')
    print('|\t', Fore.RED + 'Сохраните билет !' + Fore.WHITE, '\t\t|')
    print('-' * 41)


def by_ticket():  # покупка билета из предложенных фильмов
    for k, v in films_base.items():  # печать всех фильмов
        print(Fore.CYAN + f'Фильм: {k}' + Fore.WHITE, f'| {v[0]} ,в кинотеатре {v[1]} c {v[2]} в {v[4]} с возростным ограничением {v[5]}')
    while True:  # ввод данных пока не буден найден фильм
        film_number = int(input(Fore.GREEN + 'Номер: ' + Fore.WHITE))  # выбор фильма для покупки
        for k, v in films_base.items():
            if k == film_number:
                os.system('clear')
                print(Fore.CYAN + 'Свободно обычных мест:' + Fore.RED, v[7],
                      Fore.CYAN + '\nСвободно комфортных мест:' + Fore.RED, v[8],
                      Fore.YELLOW + '\nВыберите:\n1 | Обычное\n2 | Комфортное' + Fore.WHITE)
                while True:  # выбор места комфорт\обычное
                    seat_choose = int(input('Номер: '))
                    if seat_choose == 1:  # обычные сиденья
                        price = '5$'
                        v[7] -= 1
                        seat = 'simple'
                        with open('film_base.txt', 'w') as filehandle:
                            for k, v in films_base.items():
                                for listitem in v:
                                    filehandle.write('%s\n' % listitem)
                        break
                    elif seat_choose == 2:  # комфортные
                        v[8] -= 1
                        price = '10$'
                        seat = 'comfort'
                        with open('film_base.txt', 'w') as filehandle:
                            for k, v in films_base.items():
                                for listitem in v:
                                    filehandle.write('%s\n' % listitem)
                        break
                    else:
                        print(Fore.RED + 'Повторите ещё(1/2)' + Fore.WHITE)
                print(Fore.CYAN + f'Цена билета составит {price} желаете продолжить ?' + Fore.WHITE)  # печать стоимости
                while True:  # выбор приемлимости цены пока не будет да\нет
                    price_choose = input('(Да/Нет): ').lower()
                    if price_choose == 'да':
                        break  # выход для печати билета
                    elif price_choose == 'нет':
                        print(Fore.CYAN + 'Досвидания, будем рады вас видеть ещё !' + Fore.WHITE)
                        exit()  # выход из программы
                    else:
                        print(Fore.RED + 'Некоррекктные данные, повторите ещё (Да/Нет):' + Fore.WHITE)
                while True:
                    if seat == 'simple':  # печать билета для обычных мест
                        print_ticket(v[1], v[2], v[3], v[7], v[6], v[4], price)
                        break
                    elif seat == 'comfort':  # печать билета для комфортных мест
                        print_ticket(v[1], v[2], v[3], v[8], v[6], v[4], price)
                        break
                    else:
                        print(Fore.RED + 'Некоррекктные данные, повторите ещё:' + Fore.WHITE)
                        continue
                choose = input(Fore.YELLOW + 'Желаете преобрести ещё билет ?\n(Да/Нет): ' + Fore.WHITE).lower()
                if choose == 'да':
                    by_ticket()  # вызов рекурсии покупки билета для продолжения
                elif choose == 'нет':
                    print(Fore.CYAN + 'Досвидания, будем рады вас видеть ещё !' + Fore.WHITE)
                    exit()  # выход из программы
                else:
                    print(Fore.RED + 'Неизвестная команда, повторите ещё' + Fore.WHITE)
            else:  # если фильма нет в списке повторить ввод данных
                print(Fore.RED + 'Некоррекктные данные, повторите ещё' + Fore.WHITE)


def main():
    error = 2  # 3 попытеи ввода неправильного пароля
    os.system('clear')
    print(Fore.CYAN + '\tДобро пожаловать в ticket.by' + Fore.WHITE)
    print(Fore.YELLOW + 'У вас есть учётная запись ?' + Fore.WHITE, end='')
    choose_in_office = input('\n(Да/Нет): ').lower()  # выбор наличия аккаунта
    while True:  # ввод данных до корректных значений да\нет
        if choose_in_office == 'да':  # аккаунт в наличии
            os.system('clear')
            print(Fore.CYAN + '\tДобро пожоловать в личный кабинет' + Fore.WHITE)  # вход в личный кабинет
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            while True:
                while True:
                    film_count = len(films_base)  # длинна фильма для печати всех фильмов
                    if (login in office_base and office_base[login] == password) and (
                            login == 'admin'):  # вход только для админа
                        os.system('clear')
                        while True:  # возможность многократных манипуляций админа
                            os.system('clear')
                            print(Fore.CYAN + 'Выберите дейстивие:' + Fore.YELLOW)  # выбор действия админа
                            admin_choose = input('(Удалить/Добавить/Выйти): ').lower()
                            print('' + Fore.WHITE, end='')
                            count = 0  # счётчик для вывода
                            if admin_choose == 'удалить':  # печать доступных фильмов
                                for k, v in films_base.items():
                                    count += 1
                                    print(f'Фильм: {k} | {v[0]}')
                                try:  # исключение выхода за индекс списка фильмов
                                    number = int(input(Fore.GREEN + 'Номер: ' + Fore.WHITE))
                                    films_base.pop(number)  # удаление фильма
                                    with open('film_base.txt', 'w') as filehandle:
                                        for k, v in films_base.items():
                                            for listitem in v:
                                                filehandle.write('%s\n' % listitem)
                                except (KeyError, ValueError):
                                    print(Fore.RED + 'Такого фильма не существует, повторите ещё!' + Fore.WHITE)
                            elif admin_choose == 'добавить':
                                value = film_add(films_base)  # вызов функции возвращающий список с данными о фильме
                                print('\n', *value)
                                sure = input('Введённые данные коректны ?\n(Да/Нет): ').lower()
                                if sure == 'да':
                                    films_base[film_count + 1] = value  # добавление фильма в базу
                                    with open('film_base.txt', 'w') as filehandle:
                                        for k, v in films_base.items():
                                            for listitem in v:
                                                filehandle.write('%s\n' % listitem)
                                elif sure == 'нет':
                                    var = None
                                else:
                                    print(Fore.RED + 'Неизвестная команда' + Fore.WHITE)
                            elif admin_choose == 'выйти':
                                exit()  # выход
                    elif (login in office_base and office_base[login] == password) and (login != 'admin'):
                        os.system('clear')
                        by_ticket()  # покупка билета
                    else:  # некорректные данные
                        os.system('clear')
                        print(Fore.RED + 'Неверные данные, введите повторно' + Fore.WHITE)
                        login = input('Введите логин: ')
                        password = input('Введите пароль: ')
                        error -= 1  # 3 попытки входа в аккаунт
                    if error == 0:  # выход после трёх неудачных попыток входа
                        print(Fore.RED + 'Данные введены неверно 3 раза, выход из программы' + Fore.WHITE)
                        break
                break
            break
        elif choose_in_office == 'нет':  # неавторизированный пользователь
            os.system('clear')
            print(Fore.CYAN + '\tДобро пожаловать в создание профиля !' + Fore.WHITE)
            login = input('Введите логин: ')
            p1, p2, answer = '', '', ''
            while True:  # создание аккаунта
                if login not in office_base:
                    add_account(office_base, login)
                    with open('base.txt', 'w') as out:
                        for key, val in office_base.items():
                            out.write('{}:{}\n'.format(key, val))
                    break
                elif login in office_base:  # ошибка если логин занят
                    print(Fore.RED + 'Логин уже используется, выберите другой' + Fore.WHITE)
                    login = input('Введите логин: ')
                    add_account(office_base, login)
            main()  # после создания рекурсивная функция для потворного входа
        else:  # проверка на корректность
            while True:
                os.system('clear')
                choose_in_office = input(Fore.RED + 'Не корректная форма выберите (Да/Нет): ' + Fore.WHITE)
                if choose_in_office == 'да' or choose_in_office == 'нет':
                    break


main()