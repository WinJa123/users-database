from crud import (
    select_users,
    add_user,
    update_user,
    delete_user,
    delete_all_table_from_database,
    search_user,
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
            print('5 - Найти пользователя по ID или ФИО')
            print('6 - Добавить 15 случайных пользователей')
            print('7 - Кастомный JOIN запрос')
            print('Пустая строка - возврат в главное меню')
            action = input('Выберите (от 1 до 7): ')
            if action.isdigit() is False:
                raise ValueError(f'Ожидалось Int. Получено {type(action)}')
            
            if int(action) == 1:
                all_users = select_users()
                for i, user in enumerate(all_users, 1):

                    print(f'\n {i}. {user}\n')

            elif int(action) == 2:
                fullname = input('Введите ФИО: ').strip()
                if fullname == '':
                    print('ФИО не введено: возврат в главное меню')
                    continue

                age = input('Введите возраст: ')
                if age == '':
                    print('Возраст не введен: возврат в главное меню')
                    continue

                if age.isdigit() is False:
                    raise ValueError(f'Ожидалось Int. Получено {type(age)}')

                have_pc = input('Наличие ПК (да/нет): ')
                status_have_pc = {'да': True, '': None}.get(have_pc.replace(' ', '').lower(), False)
                if status_have_pc is True:
                    model_pc = input('Введите модель вашего ПК: ')
                answer = add_user(fullname=fullname, age=int(age), have_pc=status_have_pc, model_pc=model_pc)
                print(answer)

            elif int(action) == 3:
                all_users = select_users()
                for i, user in enumerate(all_users):

                    print(f'\n{i}. {user}\n')
                

                user_id = input('Введите ID пользователя параметры которого нужно изменить: ')
                if user_id == '':
                    print('ID не введен: возврат в главное меню')
                    continue

                if user_id.isdigit() is False:
                    raise ValueError(f'Ожидалось Int. Получено {type(user_id)}')
                
                answer = search_user(user_id)
                if answer == '':
                    print('Пользователь не найден: возврат в главное меню')
                    continue
                if answer is None:
                    print('Неизвестная ошибка: возврат в главное меню')
                    continue

                print('\nВведите параметр пользователя который нужно обновить: (1 - ФИО, 2 - Возраст, 3 - Наличие ПК)')
                print('При необходимости изменить несколько параметров - напишите подряд цифры параметров')
                parameters = input('Ввод: ')
                if parameters == '':
                    print('Параметры не введены: возврат в главное меню')
                    continue

                if parameters.isdigit() is False:
                    raise ValueError(f'Ожидалось Int. Получено {type(parameters)}')
                
                int_parameters = int(int_parameters)
                if int_parameters == 1 or int_parameters == 12 or int_parameters == 13 or int_parameters == 123:
                    fio = input('Введите новое ФИО: ')
                    if fio == '':
                        print('ФИО не может быть пустым: возврат в главное меню')
                        continue

                    if int_parameters == 12:
                        age = input('Введите новый возраст: ')
                        if age == '':
                            print('Возраст не введен: возврат в главное меню')
                            continue

                        if age.isdigit() is False:
                            raise ValueError(f'Ожидалось Int. Получено {type(age)}')
                        
                        answer = update_user(user_id, fio, int(age))
                        print(answer)
                    elif int_parameters == 13:
                        if input('Наличие ПК (да/нет): ').lower() == 'да':
                            have_pc = True
                            answer = update_user(user_id, fio, have_pc)
                            print(answer)
                        else:
                            have_pc = False
                            answer = update_user(user_id, fio, have_pc)
                            print(answer)
                    elif int_parameters == 123:
                        age = input('Введите новый возраст: ')
                        if age == '':
                            print('Возраст не введен: возврат в главное меню')
                            continue
                        
                        if age.isdigit() is False:
                            raise ValueError(f'Ожидалось Int. Получено {type(age)}')
                        
                        if input('Наличие ПК (да/нет): ').lower() == 'да':
                            have_pc = True
                            answer = update_user(user_id, fio, int(age), have_pc)
                            print(answer)
                        else:
                            have_pc = False
                            answer = update_user(user_id, fio, age, have_pc)
                            print(answer)
                    answer = update_user(user_id, fio)
                    print(answer)
                elif int_parameters == 2 or int_parameters == 23:
                    age = input('Введите новый возраст: ')
                    if age == '':
                        print('Возраст не введен: возврат в главное меню')
                        continue                                 
                                            
                    if age.isdigit() is False:
                        raise ValueError(f'Ожидалось Int. Получено {type(age)}')
                    
                    if int_parameters == 23:
                        if input('Наличие ПК (да/нет): ').lower() == 'да':
                            have_pc = True
                            answer = update_user(user_id, int(age), have_pc)
                            print(answer)
                        else:
                            have_pc = False
                            answer = update_user(user_id, age, have_pc)
                            print(answer)
                    answer = update_user(user_id, age)
                    print(answer)
                elif int_parameters == 3:
                    if input('Наличие ПК (да/нет): ').lower() == 'да':
                        have_pc = True
                        answer = update_user(user_id, have_pc)
                        print(answer)
                    else:
                        have_pc = False
                        answer = update_user(user_id, have_pc)
                        print(answer)

            
            elif int(action) == 4:
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
                            print('Возврат в главное меню')
                            continue

                    else:
                        answer = delete_user(int(user))
                        print(answer)
                else:
                    print('ID не введен: возврат в главное меню')
                    raise ValueError(f'Ожидалось (Int or "DROP ALL"). Получено {type(user)}')

            elif int(action) == 5:
                id_or_fio = input('Введите ID пользователя или полное ФИО: ').strip()
                if id_or_fio == '':
                    print('ID или ФИО не введено: возврат в главное меню')
                    continue

                answer = search_user(id_or_fio)
                print(answer)
            elif int(action) == 6:
                answer = adds_users_from_rand_fio()
                print(answer)
            elif int(action) == 7:
                answer = my_select_query()
                for i, (user, pcs) in enumerate(answer, 1):
                    print(f'\n{i}. {user} | {pcs.model_pc}\n')
            else:
                print('Выберите от 1 до 7')
                continue

        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            continue
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')