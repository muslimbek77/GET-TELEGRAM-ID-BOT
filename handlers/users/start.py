from aiogram.types import Message
from filters.admin import IsBotAdminFilter
from loader import dp,db, ADMINS
from aiogram.filters import CommandStart,Command
from keyboard_buttons import admin_keyboard,getidbutton
from aiogram import F


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
    except:
        pass
    await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz",reply_markup=getidbutton.get_id_button)



@dp.message(F.user_shared)
async def get_user_id(message: Message):
    id = message.user_shared.user_id
    text = "🏷 ID: <code>{id}</code>".format(id=id)
    await message.answer(text,reply_markup=getidbutton.get_id_button,parse_mode="html")

@dp.message(F.chat_shared)
async def get_chat_id(message: Message):
    id = message.chat_shared.chat_id
    text = "🏷 ID: <code>{id}</code>".format(id=id)
    await message.answer(text,reply_markup=getidbutton.get_id_button,parse_mode="html")


