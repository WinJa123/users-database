from sqlalchemy import select, join

from database import SessionLocal, Base, engine
from models import UsersORM, Pc, AppError, UserNotFoundError, InvalidAgeError
from rand_users import (
    generation_age,
    generation_fullname,
    generation_have_pc,
    generation_model_pc,
    generation_email_address
    )
from config import logger

 
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
                pc_user = Pc(owner_id=new_user.id, model_pc=model_pc)
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



def adds_users_from_rand_user() -> str:
    
    users = []
    pc_users = []
    
    with SessionLocal() as session:
        try:
            for _ in range(1, 16):
                email = generation_email_address()
                if email is True:
                    return 'свободные email закончились'
                new_user = UsersORM(fullname=generation_fullname(), age=generation_age(), have_pc=generation_have_pc(), email=email)
                
                users.append(new_user)
                if new_user.have_pc is True:
                    pc_user = Pc(owner_id=new_user.id, model_pc=generation_model_pc())
                    pc_users.append(pc_user)
                logger.info(f'Пользователь {[new_user]} добавлен в сессию.')

            session.add_all(users)
            session.flush()
            j = 0
            for i in pc_users:
                i.owner_id = users[j].id
                j += 1
            session.add_all(pc_users)
            session.commit()

            return logger.info('Добавлено 15 случайных пользователей.') 
                
        except Exception as err:
            
            session.rollback()

            return logger.error(err)




def my_select_query():
    with SessionLocal() as session:
        stmt = select(UsersORM, Pc).join(Pc, Pc.owner_id == UsersORM.id)
        result = session.execute(stmt)
        users = result.all()
        
        logger.info('JOIN запрос выполнен (кастомный).')
        return users


