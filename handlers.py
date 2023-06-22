from aiogram import F, Router, types, flags
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile
from aiogram.enums.parse_mode import ParseMode

import kb

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    photo = BufferedInputFile.from_file(path = f'Информация/Список городов.jpg', filename = f'Основной')
    await msg.answer_photo(
        caption = "Данный бот предназначен для сотрудников ГК РОСАТОМ и соискателей для получения информации о предприятиях в городах присутствия",
        photo = photo,
        # reply_markup=kb.main_menu,
        parse_mode = ParseMode.HTML
    )

@router.message(Command('angarsk'))
async def angarsk_info(msg: Message):
    await msg.answer(
        'Ангарск',
        reply_markup = kb.menus['Ангарск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('balakovo'))
async def balakovo_info(msg: Message):
    await msg.answer(
        'Балаково',
        reply_markup = kb.menus['Балаково'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('bilibino'))
async def bilibino_info(msg: Message):
    await msg.answer(
        'Билибино',
        reply_markup = kb.menus['Билибино'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('volgodonsk'))
async def volgodonsk_info(msg: Message):
    await msg.answer(
        'Волгодонск',
        reply_markup = kb.menus['Волгодонск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('glazov'))
async def glazov_info(msg: Message):
    await msg.answer(
        'Глазов',
        reply_markup = kb.menus['Глазов'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('dimitrovgrad'))
async def dimitrovgrad_info(msg: Message):
    await msg.answer(
        'Димитровград',
        reply_markup = kb.menus['Димитровград'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('desnogorsk'))
async def desnogorsk_info(msg: Message):
    await msg.answer(
        'Десногорск',
        reply_markup = kb.menus['Десногорск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('zheleznogorsk'))
async def zheleznogorsk_info(msg: Message):
    await msg.answer(
        'Железногорск',
        reply_markup = kb.menus['Железногорск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('zarechnyj_penza'))
async def zarechnyj_penza_info(msg: Message):
    await msg.answer(
        'Заречный (Пенза)',
        reply_markup = kb.menus['Заречный (Пенза)'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('zarechnyj_sverd'))
async def zarechnyj_sverd_info(msg: Message):
    await msg.answer(
        'Заречный (Свердловская область)',
        reply_markup = kb.menus['Заречный (Свердловская область)'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('zelenogorsk'))
async def zelenogorsk_info(msg: Message):
    await msg.answer(
        'Зеленогорск',
        reply_markup = kb.menus['Зеленогорск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('kovrov'))
async def kovrov_info(msg: Message):
    await msg.answer(
        'Ковров',
        reply_markup = kb.menus['Ковров'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('krasnokamensk'))
async def krasnokamensk_info(msg: Message):
    await msg.answer(
        'Краснокаменск',
        reply_markup = kb.menus['Краснокаменск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('kyrchatov'))
async def kyrchatov_info(msg: Message):
    await msg.answer(
        'Курчатов',
        reply_markup = kb.menus['Курчатов'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('lesnoj'))
async def lesnoj_info(msg: Message):
    await msg.answer(
        'Лесной',
        reply_markup = kb.menus['Лесной'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('novovoronezh'))
async def novovoronezh_info(msg: Message):
    await msg.answer(
        'Нововоронеж',
        reply_markup = kb.menus['Нововоронеж'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('obninsk'))
async def obninsk_info(msg: Message):
    await msg.answer(
        'Обнинск',
        reply_markup = kb.menus['Обнинск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('ozersk'))
async def ozersk_info(msg: Message):
    await msg.answer(
        'Озерск',
        reply_markup = kb.menus['Озерск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('pevek'))
async def pevek_info(msg: Message):
    await msg.answer(
        'Певек',
        reply_markup = kb.menus['Певек'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('polyarnye_zori'))
async def polyarnye_zori_info(msg: Message):
    await msg.answer(
        'Полярные Зори',
        reply_markup = kb.menus['Полярные Зори'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('sarov'))
async def sarov_info(msg: Message):
    await msg.answer(
        'Саров',
        reply_markup = kb.menus['Саров'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('seversk'))
async def seversk_info(msg: Message):
    await msg.answer(
        'Северск',
        reply_markup = kb.menus['Северск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('snezhinsk'))
async def snezhinsk_info(msg: Message):
    await msg.answer(
        'Снежинск',
        reply_markup = kb.menus['Снежинск'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('sosnovuj_bor'))
async def sosnovuj_bor_info(msg: Message):
    await msg.answer(
        'Сосновый Бор',
        reply_markup = kb.menus['Сосновый Бор'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('trehgornyj'))
async def trehgornyj_info(msg: Message):
    await msg.answer(
        'Трехгорный',
        reply_markup = kb.menus['Трехгорный'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('udomlya'))
async def udomlya_info(msg: Message):
    await msg.answer(
        'Удомля',
        reply_markup = kb.menus['Удомля'],
        parse_mode = ParseMode.HTML
    )  
@router.message(Command('energodar'))
async def energodar_info(msg: Message):
    await msg.answer(
        'Энергодар',
        reply_markup = kb.menus['Энергодар'],
        parse_mode = ParseMode.HTML
    )  

@router.callback_query(F.data == "Вернуться к выбору города")
async def input_text_prompt(clbck: None, state: FSMContext):
    photo = BufferedInputFile.from_file(path = f'Информация/Список городов.jpg', filename = f'Основной')
    await clbck.message.answer_photo(
        photo = photo,
        reply_markup=kb.main_menu,
        parse_mode = ParseMode.HTML
    )

@router.callback_query(F.data == "Нововоронеж")
async def input_text_prompt(clbck: None, state: FSMContext):
    await clbck.message.answer("Нововоронеж", reply_markup=kb.menus['Нововоронеж'])

@router.callback_query(F.data == "О городе Нововоронеж")
async def input_text_prompt(clbck: None, state: FSMContext):
    with open('Информация/Нововоронеж/О городе/Текст.html') as file_obj:
        text = file_obj.read()
    photo = BufferedInputFile.from_file(path = f'Информация/Нововоронеж/О городе/Фото.jpg', filename = f'О Нововоронеже')
    await clbck.message.answer_photo(
        caption = text,
        photo = photo,    
        reply_markup = kb.menus['Нововоронеж'],
        parse_mode = ParseMode.HTML
    )

@router.callback_query(F.data == "Места Нововоронеж")
async def input_text_prompt(clbck: None, state: FSMContext):
    with open('Информация/Нововоронеж/Места/Текст.html') as file_obj:
        text = file_obj.read()
    await clbck.message.answer(
        text,
        parse_mode = ParseMode.HTML
    )
    for i in range(10):
        with open(f'Информация/Нововоронеж/Места/Текст_{i+1:02}.html') as file_obj:
            text = file_obj.read()
        photo = BufferedInputFile.from_file(path = f'Информация/Нововоронеж/Места/Фото_{i+1:02}.jpg', filename = f'Места Нововоронежа_{i+1:02}')
        await clbck.message.answer_photo(
            caption = text,
            photo = photo, 
            parse_mode = ParseMode.HTML
        )
    with open(f'Информация/Нововоронеж/Места/Текст_11.html') as file_obj:
        text = file_obj.read()
    photo = BufferedInputFile.from_file(path = f'Информация/Нововоронеж/Места/Фото_11.jpg', filename = f'Места Нововоронежа_11')
    await clbck.message.answer_photo(
        caption = text,
        photo = photo,    
        reply_markup = kb.menus['Нововоронеж'],
        parse_mode = ParseMode.HTML
    )

@router.callback_query(F.data == "Предприятия Нововоронеж")
async def input_text_prompt(clbck: None, state: FSMContext):
    await clbck.message.answer("Какие-то предсприятия по Нововоронежу", reply_markup=kb.menus['Нововоронеж'])

@router.callback_query(F.data == "Курск")
async def input_text_prompt(clbck: None, state: FSMContext):
    await clbck.message.answer("Курск", reply_markup=kb.menus['Курск'])

@router.callback_query(F.data == "О городе Курск")
async def input_text_prompt(clbck: None, state: FSMContext):
    await clbck.message.answer("Общая инфа по Курску", reply_markup=kb.menus['Курск'])

@router.callback_query(F.data == "Места Курск")
async def input_text_prompt(clbck: None, state: FSMContext):
    await clbck.message.answer("Места Курска", reply_markup=kb.menus['Курск'])

@router.callback_query(F.data == "Предприятия Курск")
async def input_text_prompt(clbck: None, state: FSMContext):
    await clbck.message.answer("Какие-то предсприятия по Курску", reply_markup=kb.menus['Курск'])