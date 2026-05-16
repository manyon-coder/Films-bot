
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from random import choice
import asyncio

bot = Bot(token='8708838713:AAHQX3ISBZihxbfma1U30v0oYc2GrchESKM')
dp = Dispatcher()



type_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Фільм')],
        [KeyboardButton(text='Серіал')],
        [KeyboardButton(text='Мультфільм')]
    ],
    resize_keyboard=True
)

year_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='до 1990')],
        [KeyboardButton(text='1990-2000')],
        [KeyboardButton(text='2000-2010')],
        [KeyboardButton(text='2010-2020')],
        [KeyboardButton(text='2020-2026')]
    ],
    resize_keyboard=True
)

genre_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Хоррор'), KeyboardButton(text="Комедія")],
        [KeyboardButton(text='Драма'), KeyboardButton(text='Бойовик')],
        [KeyboardButton(text='Класика'), KeyboardButton(text='Детектив')]
    ],
    resize_keyboard=True
)


again_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🔄 Ще раз')],
        [KeyboardButton(text='🏠 На початок')]
    ],
    resize_keyboard=True
)


movies = [
    # ========= ФІЛЬМИ =========

    # ХОРРОР
    {"name": "Сяйво", "type": "Фільм", "genre": "Хоррор", "year": 1980},
    {"name": "Екзорцист", "type": "Фільм", "genre": "Хоррор", "year": 1973},

    {"name": "Крик", "type": "Фільм", "genre": "Хоррор", "year": 1996},
    {"name": "Я знаю, що ви зробили минулого літа", "type": "Фільм", "genre": "Хоррор", "year": 1997},

    {"name": "Пила", "type": "Фільм", "genre": "Хоррор", "year": 2004},
    {"name": "Дзвінок", "type": "Фільм", "genre": "Хоррор", "year": 2002},

    {"name": "Закляття", "type": "Фільм", "genre": "Хоррор", "year": 2013},
    {"name": "Реінкарнація", "type": "Фільм", "genre": "Хоррор", "year": 2018},

    {"name": "Варвар", "type": "Фільм", "genre": "Хоррор", "year": 2022},
    {"name": "Ні", "type": "Фільм", "genre": "Хоррор", "year": 2022},

    # КОМЕДІЯ
    {"name": "Назад у майбутнє", "type": "Фільм", "genre": "Комедія", "year": 1985},
    {"name": "Поліцейська академія", "type": "Фільм", "genre": "Комедія", "year": 1984},

    {"name": "Один вдома", "type": "Фільм", "genre": "Комедія", "year": 1990},
    {"name": "Маска", "type": "Фільм", "genre": "Комедія", "year": 1994},

    {"name": "Євротур", "type": "Фільм", "genre": "Комедія", "year": 2004},
    {"name": "Похмілля у Вегасі", "type": "Фільм", "genre": "Комедія", "year": 2009},

    {"name": "Ми — Міллери", "type": "Фільм", "genre": "Комедія", "year": 2013},
    {"name": "Джуманджі", "type": "Фільм", "genre": "Комедія", "year": 2017},

    {"name": "Барбі", "type": "Фільм", "genre": "Комедія", "year": 2023},
    {"name": "Ножі наголо 2", "type": "Фільм", "genre": "Комедія", "year": 2022},

    # ДРАМА
    {"name": "Хрещений батько", "type": "Фільм", "genre": "Драма", "year": 1972},
    {"name": "Політ над гніздом зозулі", "type": "Фільм", "genre": "Драма", "year": 1975},

    {"name": "Форрест Гамп", "type": "Фільм", "genre": "Драма", "year": 1994},
    {"name": "Зелена миля", "type": "Фільм", "genre": "Драма", "year": 1999},

    {"name": "Ігри розуму", "type": "Фільм", "genre": "Драма", "year": 2001},
    {"name": "Гладіатор", "type": "Фільм", "genre": "Драма", "year": 2000},

    {"name": "Інтерстеллар", "type": "Фільм", "genre": "Драма", "year": 2014},
    {"name": "Джокер", "type": "Фільм", "genre": "Драма", "year": 2019},

    {"name": "Оппенгеймер", "type": "Фільм", "genre": "Драма", "year": 2023},
    {"name": "Дюна 2", "type": "Фільм", "genre": "Драма", "year": 2024},

    # БОЙОВИК
    {"name": "Термінатор", "type": "Фільм", "genre": "Бойовик", "year": 1984},
    {"name": "Хижак", "type": "Фільм", "genre": "Бойовик", "year": 1987},

    {"name": "Матриця", "type": "Фільм", "genre": "Бойовик", "year": 1999},
    {"name": "Місія нездійсненна", "type": "Фільм", "genre": "Бойовик", "year": 1996},

    {"name": "Гладіатор", "type": "Фільм", "genre": "Бойовик", "year": 2000},
    {"name": "Темний лицар", "type": "Фільм", "genre": "Бойовик", "year": 2008},
    {"name": "Месники", "type": "Фільм", "genre": "Бойовик", "year": 2012},
    {"name": "Джон Вік", "type": "Фільм", "genre": "Бойовик", "year": 2014},

    {"name": "Джон Вік 4", "type": "Фільм", "genre": "Бойовик", "year": 2023},
    {"name": "Форсаж 10", "type": "Фільм", "genre": "Бойовик", "year": 2023},

    # ДЕТЕКТИВ
    {"name": "Психо", "type": "Фільм", "genre": "Детектив", "year": 1960},
    {"name": "Вікно у двір", "type": "Фільм", "genre": "Детектив", "year": 1954},

    {"name": "Сім", "type": "Фільм", "genre": "Детектив", "year": 1995},
    {"name": "Таємниці Лос-Анджелеса", "type": "Фільм", "genre": "Детектив", "year": 1997},

    {"name": "Зодіак", "type": "Фільм", "genre": "Детектив", "year": 2007},
    {"name": "Острів проклятих", "type": "Фільм", "genre": "Детектив", "year": 2010},

    {"name": "Вбивство у Східному експресі", "type": "Фільм", "genre": "Детектив", "year": 2017},
    {"name": "Дівчина з тату дракона", "type": "Фільм", "genre": "Детектив", "year": 2011},

    {"name": "Бетмен", "type": "Фільм", "genre": "Детектив", "year": 2022},
    {"name": "Ножі наголо", "type": "Фільм", "genre": "Детектив", "year": 2019},

    # ========= СЕРІАЛИ =========

    {"name": "Друзі", "type": "Серіал", "genre": "Комедія", "year": 1994},
    {"name": "Офіс", "type": "Серіал", "genre": "Комедія", "year": 2005},
    {"name": "Теорія великого вибуху", "type": "Серіал", "genre": "Комедія", "year": 2007},
    {"name": "Brooklyn 99", "type": "Серіал", "genre": "Комедія", "year": 2013},
    {"name": "Wednesday", "type": "Серіал", "genre": "Комедія", "year": 2022},

    {"name": "Breaking Bad", "type": "Серіал", "genre": "Драма", "year": 2008},
    {"name": "Корона", "type": "Серіал", "genre": "Драма", "year": 2016},
    {"name": "Ейфорія", "type": "Серіал", "genre": "Драма", "year": 2019},
    {"name": "Останні з нас", "type": "Серіал", "genre": "Драма", "year": 2023},

    {"name": "Stranger Things", "type": "Серіал", "genre": "Хоррор", "year": 2016},
    {"name": "From", "type": "Серіал", "genre": "Хоррор", "year": 2022},

    {"name": "Шерлок", "type": "Серіал", "genre": "Детектив", "year": 2010},
    {"name": "True Detective", "type": "Серіал", "genre": "Детектив", "year": 2014},

    {"name": "Гра престолів", "type": "Серіал", "genre": "Бойовик", "year": 2011},
    {"name": "Вікінги", "type": "Серіал", "genre": "Бойовик", "year": 2013},

    # ========= МУЛЬТФІЛЬМИ =========

    {"name": "Шрек", "type": "Мультфільм", "genre": "Комедія", "year": 2001},
    {"name": "Мадагаскар", "type": "Мультфільм", "genre": "Комедія", "year": 2005},
    {"name": "Міньйони", "type": "Мультфільм", "genre": "Комедія", "year": 2015},
    {"name": "Супер Маріо", "type": "Мультфільм", "genre": "Комедія", "year": 2023},

    {"name": "Король Лев", "type": "Мультфільм", "genre": "Драма", "year": 1994},
    {"name": "Вгору", "type": "Мультфільм", "genre": "Драма", "year": 2009},
    {"name": "Душа", "type": "Мультфільм", "genre": "Драма", "year": 2020},
    {"name": "Коко", "type": "Мультфільм", "genre": "Драма", "year": 2017},

    {"name": "Кораліна", "type": "Мультфільм", "genre": "Хоррор", "year": 2009},
    {"name": "Паранорман", "type": "Мультфільм", "genre": "Хоррор", "year": 2012},

    {"name": "Суперсімейка", "type": "Мультфільм", "genre": "Бойовик", "year": 2004},
    {"name": "Людина-павук: Навколо всесвіту", "type": "Мультфільм", "genre": "Бойовик", "year": 2018},

    {"name": "Рататуй", "type": "Мультфільм", "genre": "Класика", "year": 2007},
    {"name": "ВАЛЛ-І", "type": "Мультфільм", "genre": "Класика", "year": 2008},

    {"name": "Зоотрополіс", "type": "Мультфільм", "genre": "Детектив", "year": 2016},
    {"name": "Мегамозок", "type": "Мультфільм", "genre": "Детектив", "year": 2010},
]

user_choice = {}

@dp.message(Command('start'))
async def start(message: Message):
    user_choice[message.from_user.id] = {}
    await message.answer("Обери тип:", reply_markup=type_kb)

@dp.message(F.text.in_(['Фільм', 'Серіал', 'Мультфільм']))
async def choose_type(message: Message):
    user_choice[message.from_user.id] = {"type": message.text}
    await message.answer("Обери жанр:", reply_markup=genre_kb)

@dp.message(F.text.in_(['Хоррор','Комедія','Драма','Бойовик','Класика','Детектив']))
async def choose_genre(message: Message):
    user_choice[message.from_user.id]["genre"] = message.text
    await message.answer("Обери період:", reply_markup=year_kb)

def check_year(year, period):
    if period == 'до 1990':
        return year < 1990
    elif period == '1990-2000':
        return 1990 <= year <= 2000
    elif period == '2000-2010':
        return 2000 <= year <= 2010
    elif period == '2010-2020':
        return 2010 <= year <= 2020
    elif period == '2020-2026':
        return 2020 <= year <= 2026
    return False


@dp.message(F.text.in_([
    'до 1990',
    '1990-2000',
    '2000-2010',
    '2010-2020',
    '2020-2026'
]))
async def choose_year(message: Message):

    user_id = message.from_user.id

    if user_id not in user_choice:
        await message.answer("Спочатку натисни /start")
        return

    data = user_choice[user_id]
    period = message.text

    user_choice[user_id]["period"] = period

    filtered = [
        m for m in movies
        if m["type"] == data.get("type")
        and m["genre"] == data.get("genre")
        and check_year(m["year"], period)
    ]

    if filtered:
        film = choice(filtered)

        await message.answer(
            f"🎬 {film['name']} ({film['year']})"
        )

        await message.answer(
            "Що хочеш далі?",
            reply_markup=again_kb
        )

    else:
        await message.answer(
            "Нічого не знайдено 😢",
            reply_markup=again_kb
        )

@dp.message(F.text == '🔄 Ще раз')
async def again(message: Message):

    user_id = message.from_user.id

    if user_id not in user_choice:
        await message.answer("Спочатку натисни /start")
        return

    data = user_choice[user_id]

    filtered = [
        m for m in movies
        if m["type"] == data.get("type")
        and m["genre"] == data.get("genre")
        and check_year(m["year"], data.get("period"))
    ]

    if filtered:
        film = choice(filtered)

        await message.answer(
            f"🎬 {film['name']} ({film['year']})"
        )

        await message.answer(
            "Ще один?",
            reply_markup=again_kb
        )



@dp.message(F.text == '🏠 На початок')
async def restart(message: Message):

    user_choice[message.from_user.id] = {}

    await message.answer(
        "Обери тип:",
        reply_markup=type_kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


asyncio.run(main())
