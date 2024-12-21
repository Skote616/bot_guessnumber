
import asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message

Api_token='7753331216:AAEM5N_x58vNGowE-GraGW893FChxv0kiAw'
bot =Bot(token=Api_token)
dp=Dispatcher()
    
low = 1
high = 100
current_guess = None

@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    global low, high, current_guess
    low, high = 1, 100
    current_guess = (low + high) // 2  
    await message.reply("Загадайте число от 1 до 100, а я попробую его угадать!")
    await bot.send_message(message.chat.id, f"Ваше число {current_guess}? Ответьте 'больше', 'меньше' или 'да'.")

@dp.message()
async def handle_answer(message: Message):
    global low, high, current_guess

    if message.text.lower() == 'больше':
        low = current_guess + 1
    elif message.text.lower() == 'меньше':
        high = current_guess - 1
    elif message.text.lower() == 'да':
        await message.reply(f"Ура! Я угадал ваше число: {current_guess}. Хотите сыграть еще раз? Напишите /start.")
        return
    else:
        await message.reply("Пожалуйста, ответьте 'больше', 'меньше' или 'да'.")
        return

    # Проверяем, не вышел ли диапазон за пределы
    if low > high:
        await message.reply("Что-то пошло не так. Вы уверены, что загадывали число в пределах от 1 до 100? Попробуйте снова с /start.")
        return

    # Делаем новую догадку
    current_guess = (low + high) // 2
    await bot.send_message(message.chat.id, f"Ваше число {current_guess}? Ответьте 'больше', 'меньше' или 'да'.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())