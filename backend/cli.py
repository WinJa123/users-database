from crud import (
    select_users,
    add_user,
    update_user,
    delete_user,
    delete_all_table_from_database,
    adds_users_from_rand_fio,
    my_select_query
    )
from config import logger
    
@logger.catch
def menu():
    while True:
        try:
            print('1 - Получить всех пользователей')
            print('2 - Добавить пользователя')
            print('3 - Обновление данных пользователя')
            print('4 - Удаление пользователя')
            print('5 - Добавить 15 случайных пользователей')
            print('6 - Кастомный SELECT запрос')
            action = int(input('Выберите (от 1 до 6): '))
            if action == 1:
                all_users = select_users()
                for user in all_users:

                    print(f'\n{user}\n')

            elif action == 2:
                fullname = input('Введите ФИО: ').strip()
                if fullname == '':
                    print()
                    continue
                age = int(input('Введите возраст: '))

                have_pc = input('Наличие ПК (да/нет): ')
                status_have_pc = {'да': True, '': None}.get(have_pc.replace(' ', '').lower(), False)
                
                answer = add_user(fullname=fullname, age=age, have_pc=status_have_pc)
                print(answer)

            elif action == 3:
                all_users = select_users()
                for user in all_users:

                    print(f'\n{user}\n')
                

                user_id = int(input('Введите ID пользователя параметры которого нужно изменить: '))
                print('\nВведите параметр пользователя который нужно обновить: (1 - ФИО, 2 - Возраст, 3 - Наличие ПК)')
                print('При необходимости изменить несколько параметров - напишите подряд цифры параметров')
                parameters = int(input('Ввод: '))
                if parameters == 1 or parameters == 12 or parameters == 13 or parameters == 123:
                    fio = input('Введите новое ФИО: ')
                    if parameters == 12:
                        age = int(input('Введите новый возраст: '))
                        answer = update_user(user_id, fio, age)
                        print(answer)
                    elif parameters == 13:
                        if input('Наличие ПК (да/нет): ').lower() == 'да':
                            have_pc = True
                            answer = update_user(user_id, fio, have_pc)
                            print(answer)
                        else:
                            have_pc = False
                            answer = update_user(user_id, fio, have_pc)
                            print(answer)
                    elif parameters == 123:
                        age = int(input('Введите новый возраст: '))
                        if input('Наличие ПК (да/нет): ').lower() == 'да':
                            have_pc = True
                            answer = update_user(user_id, fio, age, have_pc)
                            print(answer)
                        else:
                            have_pc = False
                            answer = update_user(user_id, fio, age, have_pc)
                            print(answer)
                    answer = update_user(user_id, fio)
                    print(answer)
                elif parameters == 2 or parameters == 23:
                    age = int(input('Введите новый возраст: '))
                    if parameters == 23:
                        if input('Наличие ПК (да/нет): ').lower() == 'да':
                            have_pc = True
                            answer = update_user(user_id, age, have_pc)
                            print(answer)
                        else:
                            have_pc = False
                            answer = update_user(user_id, age, have_pc)
                            print(answer)
                    answer = update_user(user_id, age)
                    print(answer)
                elif parameters == 3:
                    if input('Наличие ПК (да/нет): ').lower() == 'да':
                        have_pc = True
                        answer = update_user(user_id, have_pc)
                        print(answer)
                    else:
                        have_pc = False
                        answer = update_user(user_id, have_pc)
                        print(answer)

            
            elif action == 4:
                all_users = select_users()
                for user in all_users:

                    print(f'\n{user}\n')
                user = input('Введите ID пользователя которого нужно удалить (DROP ALL - Удалить все таблицы): ')
                if user.isdigit() or user == 'DROP ALL':
                    if user == 'DROP ALL':
                        if input('Подтвердите удаление всех таблиц. Введите "УДАЛИТЬ ВСЕ": ') == 'УДАЛИТЬ ВСЕ':
                            delete_all_table_from_database()
                            break
                    else:
                        answer = delete_user(int(user))
                        print(answer)
                else:
                    print()
                    continue
            elif action == 5:
                answer = adds_users_from_rand_fio()
                print(answer)
            elif action == 6:
                answer = my_select_query()
                for user in answer:
                    print(f'\n{user}\n')
            else:
                print()
                continue
        except ValueError as err:
            logger.error(err)
            print()
            continue