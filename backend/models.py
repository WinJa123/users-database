from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class UsersORM(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str]
    age: Mapped[int]
    have_pc: Mapped[bool | None]
    def __repr__(self):
        return f'Users(id={self.id}, fullname={self.fullname}, age={self.age}), have_pc={self.have_pc}'
    def __str__(self):
        return f'ID: {self.id} | {self.fullname}. Возраст: {self.age}. Наличие ПК: {self.have_pc}'


class Pc(Base):
    __tablename__ = 'pcs'

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    model_pc: Mapped[str | None]
    def __repr__(self):
        return f'Pc(id={self.id} | owner_id={self.owner_id} | model_pc={self.model_pc})'
    def __str__(self):
        return f'ID: {self.id} | ID пользователя из таблицы users: {self.owner_id}. Модель ПК: {self.model_pc}'
    


class AppError(Exception):
    pass


class UserNotFoundError(AppError):
    pass


class InvalidAgeError(AppError):
    pass