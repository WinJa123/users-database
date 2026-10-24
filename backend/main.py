from database import Base, engine

from cli import menu

Base.metadata.create_all(bind=engine)

def main():
    menu()



if __name__ == '__main__':
    main()