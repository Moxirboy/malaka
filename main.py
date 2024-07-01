import asyncio

import logging

from aiogram import Bot,Dispatcher

from app.router import router
from app.test import router1
TOKEN='7426182095:AAGfJ29YxDxy1uczYyJ_JjodnHjUA0aAT78'



bot=Bot(token=TOKEN)
dp=Dispatcher()

async def main():
    dp.include_routers(router,router1)
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt :
        logging.info("exit")