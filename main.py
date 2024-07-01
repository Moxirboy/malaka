import asyncio

import logging

from aiogram import Bot,Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.router import router
from app.test import router1
TOKEN='7426182095:AAGfJ29YxDxy1uczYyJ_JjodnHjUA0aAT78'



bot=Bot(token=TOKEN)
dp=Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message:Message):
    # Send the welcome message with the inline keyboard
    print(message.from_user.full_name)
    await message.answer("Testlar felsher mutahassisligi bo'yicha atestatsiyadan o'tish uchun bir necha daqiqada 50 ta savolga\nqancha to'g'ri javob topishingizni bilib oling./test")

async def main():
    dp.include_routers(router,router1)
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt :
        logging.info("exit")