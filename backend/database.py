from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import DB_URL
engine = create_engine(
    url=DB_URL,
    echo=False
)
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
