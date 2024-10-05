import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import crud_functions


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
button_1 = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
button_3 = KeyboardButton(text = 'Купить')
button_5 = KeyboardButton(text = 'Регистрация')
kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1, button_2, button_3, button_5)
button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_1 = InlineKeyboardMarkup().add(button_3, button_4)
kb_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Product1', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product3', callback_data='product_buying'),
            InlineKeyboardButton(text='Product4', callback_data='product_buying')
        ]
    ]
    , resize_keyboard=True
)

crud_functions.initiate_db()
# crud_functions.records()
crud_functions.get_all_products()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer(reply_markup= kb_1, text='Выберите опцию:')

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора: для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.message_handler(commands= ['start'])
async def start(message):
    await message.answer('Привет', reply_markup = kb)

@dp.callback_query_handler(text= 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(height=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    await state.get_data()
    data = await state.get_data()
    OR = 10 * int(data['age']) + 6.25 * int(data['height']) - 5 * int(data['weight']) + 5
    await message.answer(f"{OR}")
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    result = crud_functions.get_all_products()
    number = 1
    for product in result:
        with open(f'foto/{product[0]}.png', "rb") as img:
            await message.answer(f'Название: {product[1]} | Описание: описание {product[2]} | Цена:'
                                 f'{product[3]}')
            await message.answer_photo(img)
            number += 1
    await message.answer(text="Выберите продукт для покупки:", reply_markup=kb_2)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    # await message.answer('Введите имя пользователя (только латинский алфавит):')
    if crud_functions.is_included(message.text) == False:
        RegistrationState.username = message.text
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    RegistrationState.email = message.text
    # await RegistrationState.email.set()
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    RegistrationState.age = message.text
    un = RegistrationState.username
    em = RegistrationState.email
    age = RegistrationState.age
    crud_functions.add_user(un, em, age)
    await message.answer('Регистрация прошла успешно')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)