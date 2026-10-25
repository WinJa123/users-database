from sqlalchemy import select, join

from database import SessionLocal, Base, engine
from models import UsersORM, Pc, AppError, UserNotFoundError, InvalidAgeError
from rand_users import generation_fio, generation_age, generation_have_pc, generation_model_pc
from config import logger

 
def select_users() -> str:
    with SessionLocal() as session:
        query = select(UsersORM)
        result = session.execute(query)
        users = result.scalars().all()

        logger.info('SELECT запрос выполнен (получение всех пользователей).')
        return users

def add_user(fullname: str, age: int, have_pc: bool, model_pc: str|None) -> str:
    with SessionLocal() as session:
        try:
            new_user = UsersORM(fullname=fullname, age=age, have_pc=have_pc)
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

def update_user(id: int, new_fio: str = '', new_age: int = -1, have_pc: bool = None) -> str:
    with SessionLocal() as session:
        try:
            user = session.get(UsersORM, id)
            if new_fio != '':
                user.fullname = new_fio
            if new_age != -1:
                user.age = new_age
            if have_pc != None:
                user.have_pc = have_pc
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


def search_user(id_or_fio: str) -> str | None:
    with SessionLocal() as session:
        try:

            if id_or_fio.isdigit() is True:
                user = session.get(UsersORM, int(id_or_fio))
                if user == None:
                    raise UserNotFoundError
                return user
            else:
                query = select(UsersORM).where(UsersORM.fullname == id_or_fio)
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



def adds_users_from_rand_fio() -> str:
    
    news_users = generation_fio()
    
    with SessionLocal() as session:
        try:
            for i in range(1, 16):
                age = generation_age()
                have_pc = generation_have_pc()
                
                user = UsersORM(fullname=news_users[i], age=age, have_pc=have_pc)
                session.add(user)
                session.flush()
                if have_pc is True:
                    pc_user = Pc(owner_id=user.id, model_pc=generation_model_pc())
                    session.add(pc_user)
                session.commit()
                logger.info(f'Пользователь {[user]} добавлен.')


            return logger.info('Добавлено 15 случайных пользователей.') 
                
        except Exception as err:
            
            session.rollback()

            return logger.error(err)




def my_select_query():
    with SessionLocal() as session:
        stmt = select(UsersORM, Pc).join(Pc, Pc.owner_id == UsersORM.id)
        result = session.execute(stmt)
        users = result.all()
        logger.info(users)
        
        logger.info('JOIN запрос выполнен (кастомный).')
        return users


