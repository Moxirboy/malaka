import asyncio

import logging

from aiogram import Bot,Dispatcher

from app.router import router
from app.test import router1
TOKEN='6810479586:AAFpX9MavDduK-9iNTpx269MkbveRXNo5Jw'



bot=Bot(token=TOKEN)
dp=Dispatcher()

async def main():
    dp.include_routers(router,router1)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        asyncio.run(main())
    except KeyboardInterrupt :
        logging.info("exit")