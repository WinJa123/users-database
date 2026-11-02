from sqlalchemy import Boolean, delete, select, join, text

from backend.database import SessionLocal, Base, engine
from backend.models import UsersORM, PcORM, AppError, UserNotFoundError, InvalidAgeError
from backend.rand_users import (
    generation_age,
    generation_fullname,
    generation_have_pc,
    generation_model_pc,
    generation_email_address
    )
from backend.config import logger

 
def select_users() -> str:
    with SessionLocal() as session:
        query = select(UsersORM)
        result = session.execute(query)
        users = result.scalars().all()

        logger.info('SELECT запрос выполнен (получение всех пользователей).')
        return users


def add_user(fullname: str, age: int, have_pc: bool, email: str, model_pc: str = None)  -> str:
    with SessionLocal() as session:
        try:
            new_user = UsersORM(fullname=fullname, age=age, have_pc=have_pc, email=email)
            session.add(new_user)
            session.flush()
            if have_pc is True:
                pc_user = PcORM(owner_id=new_user.id, model=model_pc)
                session.add(pc_user)

            
            session.commit()

            return logger.info(f'Пользователь "{[new_user]}" создан.')
        except Exception as err:
            session.rollback()

            return logger.error(err)


def update_user(id: int, new_fullname: str = '', new_age: int = -1, have_pc: bool = None, email: str = '') -> str:
    with SessionLocal() as session:
        try:
            user = session.get(UsersORM, id)
            if new_fullname != '':
                user.fullname = new_fullname
            if new_age != -1:
                user.age = new_age
            if have_pc != None:
                user.have_pc = have_pc
            if email != '':
                user.email = email
            session.commit()

            return logger.info('Изменения сохранены.')
        except Exception as err:
            session.rollback()

            return logger.error(err)


def delete_user(user_id: int) -> str:
    with SessionLocal() as session:
        user = session.get(UsersORM, user_id)
        if user is not None:
            session.delete(user)
            session.commit()

            return logger.info(f'Пользователь "{user.fullname}" удален.')
        else:

            return logger.warning('Пользователь не найден.')


def delete_all_table_from_database() -> None:
    Base.metadata.drop_all(bind=engine)

def delete_all_users() -> None:
    with SessionLocal() as session:

        session.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE;"))
        session.commit()

def search_user(id_or_fullname: str) -> str | None:
    with SessionLocal() as session:
        try:

            if id_or_fullname.isdigit() is True:
                user = session.get(UsersORM, int(id_or_fullname))
                if user == None:
                    raise UserNotFoundError
                return user
            else:
                query = select(UsersORM).where(UsersORM.fullname == id_or_fullname)
                result = session.execute(query)
                user = result.scalars().first()
                if user is None:
                    raise UserNotFoundError
                logger.info('SELECT запрос выполнен (Поиск пользователя).')
                return user
        except UserNotFoundError:
            logger.warning('Пользователь не найден.')
            return ''
        except AppError:
            logger.warning('Незивестная ошибка в работе приложения')
            return None
        except Exception as err:
            logger.warning(f'Ошибка Exception - {err}')
            return None


def search_check_for_duplicates(fullname_or_email: str) -> Boolean:
    with SessionLocal() as session:
        if fullname_or_email.endswith(('@gmail.com', '@mail.ru', '@yandex.ru')) is True:
            query = select(UsersORM).where(UsersORM.email == fullname_or_email)
        else:
            query = select(UsersORM).where(UsersORM.fullname == fullname_or_email)
        result = session.execute(query)
        if result.scalars().first() is None:
            return False
        return True

    
def adds_users_from_rand_user(quantity_users: int) -> str:
    
    users = []
    pc_users = []
    
    with SessionLocal() as session:
        try:
            for _ in range(1, quantity_users + 1): #! Добавить: выбор количества добавленных пользователей
                email = generation_email_address()
                if email is True:
                    return 'свободные email закончились'
                new_user = UsersORM(fullname=generation_fullname(), age=generation_age(), have_pc=generation_have_pc(), email=email)
                
                users.append(new_user)
                
                logger.debug(f'Пользователь {[new_user]} добавлен в список.')
            session.add_all(users)
            session.flush()   
            for user in users:
                if user.have_pc is True:
                    pc_user = PcORM(owner_id=user.id, model=generation_model_pc())
                    pc_users.append(pc_user)
                    logger.debug(f'Пользователь {[user.fullname]} с моделью пк {pc_user.model} добавлен в список')

            session.add_all(pc_users)
            session.commit()

            return logger.info(f'Добавлено {quantity_users} случайных пользователей.') 
                
        except Exception as err:
            
            session.rollback()

            return logger.error(err)


def my_select_query() -> list:
    with SessionLocal() as session:
        query = select(UsersORM, PcORM).join(PcORM, PcORM.owner_id == UsersORM.id)
        result = session.execute(query)
        users = result.all()
        
        logger.info('JOIN запрос выполнен (кастомный).')
        return users


def filter_query(query_number: int) -> list:    #? query_number: 1 - group id | 2 - group fullname | 3 - group age
    with SessionLocal() as session:
        if query_number == 1:
            query_group = UsersORM.id
        elif query_number == 2:
            query_group = UsersORM.fullname
        else:
            query_group = UsersORM.age

        query = (
            select(UsersORM)
            .order_by(query_group)
        )
        result = session.execute(query)
        users_group_fullname = result.scalars().all()

        return users_group_fullname