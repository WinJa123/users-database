from sqlalchemy import select

from database import SessionLocal, Base, engine
from models import UsersORM
from rand_users import generation_fio, generation_age, generation_have_pc

 
def select_users() -> str:
    with SessionLocal() as session:
        query = select(UsersORM)
        result = session.execute(query)
        users = result.scalars().all()

        return users

def add_user(fullname: str, age: int, have_pc: bool) -> str:
    with SessionLocal() as session:
        try:
            new_user = UsersORM(fullname=fullname, age=age, have_pc=have_pc)
            session.add(new_user)
            session.commit()
            return 'Данные сохранены'
        except Exception as err:
            session.rollback()
            return f'Error: {err}'

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
            return 'Изменения сохранены!'
        except Exception as err:
            session.rollback()
            return f'Error: {err}'


def delete_user(user_id: int) -> str:
    with SessionLocal() as session:
        user = session.get(UsersORM, user_id)
        if user is not None:
            session.delete(user)
            session.commit()
            return f'Пользователь {user.fullname} удален'
        else:
            return 'Пользователь не найден'

def delete_all_table_from_database() -> None:
    Base.metadata.drop_all(bind=engine)

def adds_users_from_rand_fio() -> str:
    
    news_users = generation_fio()
    
    with SessionLocal() as session:
        try:
            for i in range(1, 16):
                age = generation_age()
                have_pc = generation_have_pc()
                user = UsersORM(fullname=news_users[i], age=age, have_pc=have_pc)
                session.add(user)
                session.commit()

            return 'УСПЕШНО'
                
        except Exception as err:
            
            session.rollback()
            return f'Error: {err}'




def my_select_query():
    with SessionLocal() as session:
        query = select(UsersORM).select_from(UsersORM).filter(UsersORM.have_pc.contains(1)).group_by(UsersORM.fullname)
        result = session.execute(query)
        users = result.scalars().all()
        return users
