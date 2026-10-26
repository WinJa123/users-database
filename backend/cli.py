from crud import (
    select_users,
    add_user,
    update_user,
    delete_user,
    delete_all_table_from_database,
    search_user,
    adds_users_from_rand_user,
    my_select_query
    )
from config import logger
from models import FIODuplicateError, EmailDuplicateError, InvalidAgeError
    
@logger.catch
def menu():
    while True:
        try:
            print('1 - Получить всех пользователей')
            print('2 - Добавить пользователя')
            print('3 - Обновление данных пользователя')
            print('4 - Удаление пользователя')
            print('5 - Найти пользователя по ID или ФИО')
            print('6 - Фильры/Сортировка')
            print('7 - Добавить 15 случайных пользователей')
            print('8 - Кастомный JOIN запрос')
            print('Пустая строка - возврат в главное меню')
            action = input('Выберите (от 1 до 8): ')
            if action.isdigit() is False:
                raise ValueError(f'Ожидалось Int. Получено {type(action)}')
            
            if int(action) == 1:
                cli_select_users()

            elif int(action) == 2:
                cli_add_user()

            
            elif int(action) == 3:
                cli_update_user()
            
            elif int(action) == 4:
                if cli_delete_user() == 'DROP ALL TABLES':
                    return
                

            elif int(action) == 5:
                cli_search_user()

            elif int(action) == 6:
                cli_filter_sort_users()
                    
                    
            elif int(action) == 7:
                cli_adds_users_from_rand_user()
            elif int(action) == 8:
                cli_castom_join_select()
           
            else:
                print('Выберите от 1 до 8')
                continue



        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            continue
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')




def cli_select_users() -> None:
    while True:
        try:
            all_users = select_users()
            for i, user in enumerate(all_users, 1):
                print(f'\n {i}. {user}\n')
            return
        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            return
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')
            return

def cli_add_user() -> None:
    model_pc = None
    while True:
        try:
            fullname = input('Введите ФИО: ').strip()
            all_users = select_users()
            for user in all_users:
                if fullname == user.fullname:
                    raise FIODuplicateError('Пользователь с таким ФИО уже существует')
                
            if fullname == '':
                print('ФИО не введено: возврат в главное меню')
                return
            while True:
                try:
                    age = input('Введите возраст (Введите -1 что бы отменить операцию и выйти): ')
                    if age == '':
                        print('Ошибка: возраст не введен. Введите возраст')
                        continue
                    if age == '-1':
                        print('Возврат в главное меню')
                        return
                    
                    if age.isdigit() is False and '-' in age == False:
                        raise ValueError(f'Ожидалось Int. Получено {type(age)}')
                    
                    if '-' in age or int(age) > 120:
                        raise InvalidAgeError('Неверный возраст')
                     
                except InvalidAgeError as err:
                    logger.error(f'InvalidAgeError: {err}')
                    continue
                
                have_pc = input('Наличие ПК (да/нет): ')
                status_have_pc = {'да': True, '': None}.get(have_pc.replace(' ', '').lower(), False)
                if status_have_pc is True:
                    model_pc = input('Введите модель ПК: ')
                while True:
                    try:
                        
                        email_address = input('Введите email (@gmail.com, @mail.ru, @yandex.ru): ')
                        if email_address.endswith(('@gmail.com', '@mail.ru', '@yandex.ru')) is True:
                            for user in all_users:
                                if email_address == user.email:
                                    raise EmailDuplicateError('Пользователь с такой почтой уже существует')
                                    
                            answer = add_user(fullname=fullname, age=int(age), have_pc=status_have_pc, model_pc=model_pc, email=email_address)
                            print(answer)
                            return
                        
                        else:
                            print('Данный тип почты не поддерживается')
                            continue
                    except EmailDuplicateError as err:
                        logger.error(f'EmailDuplicateError: {err}')
                        continue

        
        except FIODuplicateError as err:
            logger.error(f'FIODuplicateError: {err}')
            continue

        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            return
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')
            return  

def cli_update_user() -> None:
    while True:
        try:
            fio = ''
            age = -1
            have_pc = None
            email = ''

            all_users = select_users()
            for i, user in enumerate(all_users, 1):

                print(f'\n{i}. {user}\n')
            

            user_id = input('Введите ID пользователя параметры которого нужно изменить: ')
            if user_id == '':
                print('ID не введен: возврат в главное меню')
                return

            if user_id.isdigit() is False:
                raise ValueError(f'Ожидалось Int. Получено {type(user_id)}')
            
            answer = search_user(user_id)
            if answer == '':
                print('Пользователь не найден: возврат в главное меню')
                continue
            if answer is None:
                print('Неизвестная ошибка: возврат в главное меню')
                return

            print('\nВведите параметр пользователя который нужно обновить: (1 - ФИО, 2 - Возраст, 3 - Наличие ПК, 4 - email)')
            print('При необходимости изменить несколько параметров - напишите подряд цифры параметров')
            parameters = input('Ввод: ')
            if parameters == '':
                print('Параметры не введены: возврат в главное меню')
                return

            if parameters.isdigit() is False:
                raise ValueError(f'Ожидалось Int. Получено {type(parameters)}')
            
            if '1' in parameters:
                while True:
                    try:
                        fio = input('Введите новое ФИО: ')
                        if fio == '':
                            print('ФИО не может быть пустым: возврат в главное меню')
                            return
                        
                        for user in all_users:
                            if fio == user.fullname:
                                raise FIODuplicateError('Пользователь с таким ФИО уже существует')
                        break
                    except FIODuplicateError as err:
                        logger.error(f'FIODuplicateError: {err}')
                        continue

            if '2' in parameters:
                while True:
                    try:
                        age = input('Введите новый возраст: ')
                        if age == '':
                            print('Возраст не введен: возврат в главное меню')
                            return

                        if age.isdigit() is False and '-' in age == False:
                            raise ValueError(f'Ожидалось Int. Получено {type(age)}')
                        
                        if '-' in age or int(age) > 120:
                            raise InvalidAgeError('Неверный возраст')
                        break
                    except InvalidAgeError as err:
                        logger.error(f'InvalidAgeError: {err}')
                        continue
            if '3' in parameters:
                if input('Наличие ПК (да/нет): ').lower() == 'да':
                    have_pc = True
                else:
                    have_pc = False
            if '4' in parameters:
                while True:
                    try:
                        email = input('Введите новый email: ')
                        if email.endswith(('@gmail.com', '@mail.ru', '@yandex.ru')) is False:
                            print('Данный тип почты не поддерживается')
                            continue
                        for user in all_users:
                            if email == user.email:
                                raise EmailDuplicateError('Пользователь с такой почтой уже существует')
                        break
                    except EmailDuplicateError as err:
                        logger.error(f'EmailDuplicateError: {err}')
                        continue

            answer = update_user(id=user_id, new_fio=fio, new_age=age, have_pc=have_pc, email=email)
            return
        
        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            return
        
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')
            return

def cli_delete_user() -> None | str:
    while True:
        try:
            all_users = select_users()
            for user in all_users:

                print(f'\n{user}\n')
            user = input('Введите ID пользователя которого нужно удалить (DROP ALL - Удалить все таблицы): ')
            if user == '':
                print('ID не введено: возврат в главное меню')
                return
            
            if user.isdigit() or user == 'DROP ALL':
                if user == 'DROP ALL':
                    if input('Подтвердите удаление всех таблиц. Введите "УДАЛИТЬ ВСЕ": ') == 'УДАЛИТЬ ВСЕ':
                        delete_all_table_from_database()
                        return 'DROP ALL TABLES'
                    else:
                        print('Возврат в главное меню')
                        return

                else:
                    answer = delete_user(int(user))
                    print(answer)
                    return
                
            else:
                print('ID не введен: возврат в главное меню')
                raise ValueError(f'Ожидалось (Int or "DROP ALL"). Получено {type(user)}')
        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            return
        
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')
            return

def cli_search_user() -> None:
    while True:
        try:
            id_or_fio = input('Введите ID пользователя или полное ФИО (Нажмите "Enter" для возврата в главное меню): ').strip()
            if id_or_fio == '':
                print('ID или ФИО не введено: возврат в главное меню')
                return

            answer = search_user(id_or_fio)
            print(answer)

        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            return
        
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')
            return

def cli_filter_sort_users() -> None:            #! НЕ ДОДЕЛАНО, ФИЛЬТРАЦИЯ ПОЛЬЗОВАТЕЛЕЙ
    while True:
        try:
            print('1 - Отсортировать по ID')
            print('2 - Отсортировать по имени')
            print('3 - Отсортировать по возрасту')
            answer_filter = input('Выбор: ')
            if answer_filter.isdigit() is False:
                print('Ошибка ввода: возврат в главное меню')
                raise ValueError(f'Ожидалось (Int or "DROP ALL"). Получено {type(user)}')
            if int(answer_filter) == 1:
                all_users = select_users()
                for i, user in enumerate(all_users, 1):
                    print(f'\n {i}. {user}\n')

        except ValueError as err:
            logger.error(f'Ошибка ValueError | {err}')
            print()
            return
        
        except Exception as err:
            logger.error(f'Неизвестная ошибка Exception - {err}')
            return

def cli_adds_users_from_rand_user() -> None:
    answer = adds_users_from_rand_user()
    if answer == 'свободные email закончились':
        logger.warning('Свободные Email закончились')        
    print(answer)

def cli_castom_join_select() -> None:
    answer = my_select_query()
    for i, (user, pcs) in enumerate(answer, 1):
        print(f'\n{i}. {user} | {pcs.owner_id} - {pcs.model_pc}\n')