from colorama import Fore, Back, Style
import os

#сортировка базы фильмов по ключам

#ФУНКЦИИ
def you_sure(global_choose):
	os.system('clear')
	choose = input(Fore.YELLOW +'Желаете продолжить ?\n(Да/Нет): ' + Fore.WHITE).lower()
	if choose == 'да':
		global_choose = 'да'
		return global_choose
	elif choose == 'нет':
		print(Fore.RED + 'Выход из программы' + Fore.WHITE)
		exit()
	else:
		print(Fore.RED + 'Неизвестная команда, повторите ещё' + Fore.WHITE)

def film_add():
	os.system('clear')
	value = []
	s = ''
	# индексы(1: фильм, 2: кинотеатр, 3: начало, 4: конец, 5: время, 6: возраст, 7: зал, 8: места)
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
	s = input('Введите зал: ').title()
	value.append(s)
	s = int(input('Введите количество мест: '))
	value.append(s)
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



#БАЗА
office_base = {'admin': '1111'}
films_base = {1: ['Бонд 3', 'Аврора', '30.10.2021', '15.11.2021', '12:00', '18+', 'Малый зал', 30], 2: ['Веном 2', 'Аврора', '01.11.2021', '28.11.2021','18:30', '16+', 'Большой зал', 20]}

os.system('clear')
# ВХОД
print(Fore.CYAN + '\tДобро пожаловать в ticket.by' + Fore.WHITE)
print(Fore.YELLOW + 'У вас есть учётная запись ?' + Fore.WHITE, end = '')
choose_in_office = input('\n(Да/Нет): ').lower()
error = 2 #ОШИБКА ВХОДА 2(ПОПЫТКИ)
while True:
	if choose_in_office == 'да':
		os.system('clear')
		print(Fore.CYAN + '\tДобро пожоловать в личный кабинет' + Fore.WHITE)
		login = input('Введите логин: ')
		password = input('Введите пароль: ')
		
		while True:
			while True:
				film_count = len(films_base)
				
				if (login in office_base and office_base[login] == password) and (login == 'admin'):
					while True:
						os.system('clear')
						admin_choose = input('Выберите дейстивие:\n(Удалить/Добавить): ').lower()
						count = 0
						if admin_choose == 'удалить':
							for k, v in films_base.items():
								count += 1
								print(f'Фильм: {k} | {v[0]}')
							number = int(input(Fore.GREEN + 'Номер: ' + Fore.WHITE))
							films_base.pop(number)
							break

						elif admin_choose == 'добавить':
							while True:
								value = film_add()
								print('\n', *value)
								shure = input('Введённые данные коректны ?\n(Да/Нет): ').lower()
								if shure == 'да':
									films_base[film_count + 1] = value
									break
								elif shure == 'нет':
									None
								else:
									print('Неизвестная команда')
							break
					you_sure(choose_in_office)		
				
				

				elif (login in office_base and office_base[login] == password) and (login != 'admin'):
					count = 0
					print(Fore.YELLOW + 'Выберите номер фильм для продолжения: ' + Fore.WHITE)
					for k, v in films_base.items():
						count += 1
						print(f'Фильм: {k} | {v[0]}, в кинотеатре {v[1]} c {v[2]} по {v[3]} в {v[4]} с возростным ограничением {v[5]}')
					number = input(Fore.GREEN + 'Номер: ' + Fore.WHITE)
					break


				else:
					os.system('clear')
					print(Fore.RED + 'Неверные данные, введите повторно' + Fore.WHITE)
					login = input('Введите логин: ')
					password = input('Введите пароль: ')
					error -= 1

				
				if error == 0:
					print(Fore.RED + "Данные введены неверно 3 раза, выход из программы" + Fore.WHITE)
					break
			break
		break


	elif choose_in_office == 'нет':
		os.system('clear')
		print(Fore.CYAN + '\tДобро пожаловать в создание профиля !' + Fore.WHITE)
		login = input('Введите логин: ')
		p1, p2, answer = '', '', ''
		while True:
			if login not in office_base:
				add_account(office_base, login)
				break
				
			elif login in office_base:
				print(Fore.RED + 'Логин уже используется, выберите другой' + Fore.WHITE) 
				add_account(office_base, login)


		
		choose_in_office = you_sure(choose_in_office)
	
	else:
		while True:
			os.system('clear')
			choose_in_office = input(Fore.RED + 'Не корректная форма выберите (Да/Нет): ' + Fore.WHITE)
			if choose_in_office == 'да' or choose_in_office == 'нет':
				break


print(login)
print(films_base)
print(office_base)