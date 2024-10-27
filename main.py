import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.router import router
from app.test import router1

TOKEN = '7426182095:AAGfJ29YxDxy1uczYyJ_JjodnHjUA0aAT78'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Bot handler
@dp.message(CommandStart())
async def cmd_start(message: Message):
    print(message.from_user.full_name)
    await message.answer(
        "Testlar felsher mutahassisligi bo'yicha atestatsiyadan o'tish uchun bir necha daqiqada 50 ta savolga\n"
        "qancha to'g'ri javob topishingizni bilib oling./test"
    )

# Web server handler
async def handle(request):
    return web.Response(text="Welcome to the simple web server!")

# Function to create and run the web app
async def web_app():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 4000)
    await site.start()

# Main function to run both bot and web server
async def main():
    # Start both the bot and web server
    dp.include_routers(router, router1)
    
    # Start web server in the background
    asyncio.create_task(web_app())

    # Start the bot's polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("exit")

