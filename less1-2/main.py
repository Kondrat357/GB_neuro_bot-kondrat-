import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
import re
from keyboard import kb1, kb2
from random_fox import fox
from random import randint


API_TOKEN = config.token


# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)


# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
 name = message.chat.first_name
 await message.answer(f"Привет, {name}, Я Эхобот" , reply_markup=kb1)


@dp.message(Command("info"))
async def cmd_info(message: types.Message):
 await message.reply("Я умею повторять")


@dp.message(Command("fox"))
@dp.message(Command("лиса"))
@dp.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    img_fox = fox()
    await message.reply(f"Держи Лису")
    await message.answer_photo(photo=img_fox)

@dp.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
        number = randint(1, 10)
        await message.answer(f"{number}")


@dp.message(Command("bye"))
async def cmd_bye(message: types.Message):
 await message.reply("очень жаль, что ты уходишь", reply_markup=kb2)



@dp.message(F.text)
async def msg_handler(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
# Фильтрация имени пользователя
    if not re.match("^[a-zA-Zа-яА-ЯёЁ ]*$", name):
        name = "пользователь"
# Замена на безопасное значение
    if 'привет' in msg_user:
        await message.answer(f"Ну привет, {name}")
    elif msg_user == 'пока':
        await message.answer("зряяяяя")
    else:
        await message.answer(message.text)
    if "ты кто" in msg_user:
        await message.answer_dice(emoji="🎲")
    #else:
        #await message.answer(f'Я не понимаю')
        


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())