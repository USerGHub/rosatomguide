from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

city_commands = {
    'angarsk' : 'Ангарск',
    'balakovo' : 'Балаково',
    'bilibino' : 'Билибино',
    'volgodonsk' : 'Волгодонск',
    'glazov' : 'Глазов',
    'dimitrovgrad' : 'Димитровград',
    'desnogorsk' : 'Десногорск',
    'zheleznogorsk' : 'Железногорск',
    'zarechnyj_penza' : 'Заречный (Пенза)',
    'zarechnyj_sverd' : 'Заречный (Свердловская область)',
    'zelenogorsk' : 'Зеленогорск',
    'kovrov' : 'Ковров',
    'krasnokamensk' : 'Краснокаменск',
    'kyrchatov' : 'Курчатов',
    'lesnoj' : 'Лесной',
    'novovoronezh' : 'Нововоронеж',
    'obninsk' : 'Обнинск',
    'ozersk' : 'Озерск',
    'pevek' : 'Певек',
    'polyarnye_zori' : 'Полярные Зори',
    'sarov' : 'Саров',
    'seversk' : 'Северск',
    'snezhinsk' : 'Снежинск',
    'sosnovuj_bor' : 'Сосновый Бор',
    'trehgornyj' : 'Трехгорный',
    'udomlya' : 'Удомля',
    'energodar' : 'Энергодар',
}
main_menu = [
    [InlineKeyboardButton(text=city,callback_data=city) for city in list(city_commands.values())],
]

main_menu = InlineKeyboardMarkup(inline_keyboard = main_menu)

menus = {}
for city in list(city_commands.values()):
    menu = [
        [InlineKeyboardButton(text=f"О городе",
            callback_data=f"О городе {city}")],
        [InlineKeyboardButton(text=f"Места",
            callback_data=f"Места {city}"),
        InlineKeyboardButton(text=f"Предприятия",
            callback_data=f"Предприятия {city}")],
        [InlineKeyboardButton(text=f"Образование",
            callback_data=f"Образование {city}"),
        InlineKeyboardButton(text=f"Жилой сектор",
            callback_data=f"Жилой сектор {city}")],
        [InlineKeyboardButton(text=f"Спорт",
            callback_data=f"Спорт {city}"),
        InlineKeyboardButton(text=f"Экология",
            callback_data=f"Экология {city}")],
        # [InlineKeyboardButton(text=f"Вернуться к выбору города",
        #     callback_data=f"Вернуться к выбору города")],
    ]
    menu = InlineKeyboardMarkup(inline_keyboard = menu)
    menus[city] = menu