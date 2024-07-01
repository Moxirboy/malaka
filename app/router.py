
import asyncio

from aiogram import  F, Router, types
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,CallbackQuery

from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext

import requests
async def cmd_start(message:Message):
    await message.answer("hello",
                         reply_markup=kb.inline)


import app.keyboards as kb


class Reg(StatesGroup):
     name=State()
     number=State()
     test=State()
     end=State()
router=Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    # Send the welcome message with the inline keyboard
    await message.answer(chat_id=-4243210915,text=message.from_user.username+"\n"+message.from_user.full_name)
    await message.answer("Testlar felsher mutahassisligi bo'yicha atestatsiyadan o'tish uchun bir necha daqiqada 50 ta savolga\nqancha to'g'ri javob topishingizni bilib oling./test")

