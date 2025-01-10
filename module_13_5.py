from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import  State,StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import asyncio



api='8089324281:AAGV7_H0p_1J_z1YiprgbEvl7PT71pozGAU'
bot=Bot(token=api)
dp=Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb=ReplyKeyboardMarkup(resize_keyboard=True)
buttons=['Рассчитать','Информация']
kb.add(*buttons)

@dp.message_handler(commands=['start'])
async def main_menu(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.',reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first = message.text)
    await  message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await  message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await  state.get_data()

    await  message.answer(f"Ваша норма калорий "
                          f"{int(data['first'])*5+int(data['second'])*6.25+int(data['third'])*10-161}")

    await  state.finish()

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)