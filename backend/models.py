from database import Base
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