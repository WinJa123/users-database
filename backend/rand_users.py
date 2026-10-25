import random

firstname_man = [
    'Александр', 'Сергей', 'Дмитрий', 'Алексей',
    'Андрей', 'Владимир', 'Максим', 'Иван',
    'Евгений', 'Николай', 'Михаил', 'Артем',
    'Кирилл', 'Даниил', 'Олег', 'Игорь',
    'Роман', 'Денис', 'Антон', 'Павел',
    'Виктор', 'Илья', 'Никита', 'Тимофей',
    'Глеб'

    ]
firstname_woman = [
    'Елена', 'Ольга', 'Наталья', 'Татьяна',
    'Анна', 'София', 'Анна', 'Ева',
    'Мария', 'Анастасия', 'Екатерина', 'Ксения',
    'Дарья', 'Виктория', 'Алина', 'Полина',
    'Юлия', 'Кристина', 'Алиса', 'Вероника',
    'Валерия', 'Елизавета', 'Маргарита', 'Ирина'
    ]
lastname = [
    'Иванов', 'Смирнов', 'Кузнецов', 'Попов',
    'Васильев', 'Петров', 'Соколов', 'Михайлов',
    'Фёдоров', 'Павлов', 'Романов', 'Никитин',
    'Ильин', 'Антонов', 'Борисов', 'Карпов',
    'Степанов', 'Трофимов', 'Мартынов', 'Григорьев',
    'Гончаров', 'Алексеев', 'Яковлев', 'Дмитриев',
    'Егоров', 'Морозов', 'Волков', 'Лебедев',
    'Козлов', 'Новиков', 'Белов', 'Киселев',
    'Макаров', 'Андреев', 'Зайцев', 'Сергеев',
    'Тарасов', 'Беляев', 'Поляков',
    ]
surname_man = [
    'Александрович', 'Владимирович',
    'Николаевич', 'Сергеевич',
    'Викторович', 'Алексеевич',
    'Дмитриевич', 'Михайлович',
    'Иванович', 'Андреевич'
    ]
surname_woman = [
    'Александровна', 'Владимировна',
    'Николаевна', 'Сергеевна',
    'Викторовна', 'Алексеевна',
    'Дмитриевна', 'Михайловна',
    'Ивановна', 'Андреевна'
    ]
gender = ['М', 'Ж']
have_pc = [True, False, None]


pc_models = [
    "Lenovo",
    "Huawei",
    "ASUS",
    "Acer",
    "Apple",
    "MSI",
    "HP",
    "Dell",
    "Honor",
    "Xiaomi",
    "Infinix",
    "Tecno",
    "Gigabyte",
    "Samsung",
    "Razer"
]


def generation_fio() -> list:
    users = []
    x = 0
    while x <= 15:
        if random.choice(gender) == 'М':
            user = f'{random.choice(lastname)} {random.choice(firstname_man)} {random.choice(surname_man)}'
            users.append(user)
        else:
            user = f'{random.choice(lastname)}a {random.choice(firstname_woman)} {random.choice(surname_woman)}'
            users.append(user)
        users = list(set(users))
        x = len(users)
    return users
def generation_age() -> int:
    return random.randint(10, 86)
def generation_have_pc() -> bool:
    return random.choice(have_pc)
def generation_model_pc() -> str:
    return random.choice(pc_models)