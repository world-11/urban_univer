import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
button_1 = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1, button_2)
button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_1 = InlineKeyboardMarkup().add(button_3, button_4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

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

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)