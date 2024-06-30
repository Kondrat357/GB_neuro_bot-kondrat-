from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.utils.random_fox import fox
from less3.keyboards.keyboard import kb1, kb2
from random import randint
import re


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет, {name}, Я Эхобот", reply_markup=kb1)


@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Я умею повторять, Могу показать лису, а также могу помочь выбрать профессию, понимаю слова: привет, пока, покажи Лису")



@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    img_fox = fox()
    await message.reply(f"Держи Лису")
    await message.answer_photo(photo=img_fox)


@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
        number = randint(1, 10)
        await message.answer(f"{number}")


@router.message(Command("bye"))
async def cmd_bye(message: types.Message):
    await message.reply("очень жаль, что ты уходишь", reply_markup=kb2)


@router.message(F.text)
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
    # else:
    # await message.answer(f'Я не понимаю')




