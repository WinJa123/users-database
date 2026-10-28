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
middlename_man = [
    'Александрович', 'Владимирович',
    'Николаевич', 'Сергеевич',
    'Викторович', 'Алексеевич',
    'Дмитриевич', 'Михайлович',
    'Иванович', 'Андреевич'
    ]
middlename_woman = [
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

email_beginning = [
    "vash.smith", "uefi.doe.99", "dev_wizard", "mant.ivala", "cyber_ninja",
    "tech.enthusiast", "ret_green", "coffeelover88", "digital_nomad", "pixel_perfect",
    "wwwErretivi.k", "luna_eclipse", "code_runner", "elips.bright", "shadow_walker",
    "sky_line_2026", "maxage_v", "creative_mind", "nature.seeker", "alpha_omega", "razrab_dev",
    "new_star", "matrix_reloaded", "ulstre.miller", "quantum_leap", "art_explorer", "palka_b",
    "neon_light", "juse.soft", "urban_explorer",  "green_forest", "andmilk_rock", "sweet_cherry",
    "data_science_pro", "nashi_w", "night_owl_9", "future_vision", "ignor_tech", "sunny_day_in",
    "space_traveler", "vicitisa_secret", "blue_ocean", "motion_design", "arts_king", "silver_lining",
    "cyber_security", "li_mona", "gold_rush", "time_traveler", "vlast_sharp", "happy_camper", "code_master_77",
    "iqist_sun", "wind_of_change", "magic_wand", "konFan_v", "velvet_sky", "deep_blue", "svet_m",
    "phoenix_rise", "logic_bomb", "depla_power", "amber_glow", "infinite_loop", "tatatata_sasa", "silent_storm",
    "web_architect", "milkas_pro", "cosmic_dust", "lucky_strike", "elpa_t", "morning_dew", "crypto_king",
    "rosja_build", "star_gazer", "cloud_strife", "alkashna_beauty", "wild_card", "byte_me", "rawraw_drive", "ocean_breeze",
    "fire_starter", "ksenia_joy", "iron_clad", "pixel_art", "nitka_sky", "golden_ratio", "code_artisan", "vlastni_rose",
    "thunder_bolt", "mind_palace", "yury_mind", "emerald_city", "it_guru_2026", "darQ_dream", "frost_bite",
    "vector_graph", "oleole_prime", "margansovka_wave", "sound_wave"
]

email_last = ['@gmail.com', '@mail.ru', '@yandex.ru']


def generation_fullname() -> str:
    if random.choice(gender) == 'М':
        return f'{random.choice(lastname)} {random.choice(firstname_man)} {random.choice(middlename_man)}'
    else:
        return f'{random.choice(lastname)}а {random.choice(firstname_woman)} {random.choice(middlename_woman)}'

def generation_age() -> int:
    return random.randint(10, 86)

def generation_have_pc() -> bool:
    return random.choice(have_pc)

def generation_model_pc() -> str:
    return random.choice(pc_models)

def generation_email_address() -> str | bool:
    if len(email_beginning) == 0:
        return True
    rand_email_beginning = random.choice(email_beginning)
    email_beginning.remove(rand_email_beginning)
    
    return rand_email_beginning + random.choice(email_last)
