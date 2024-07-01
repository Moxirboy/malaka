
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


@router.message(Command('help'))
async def get_help(message:Message):
    await message.answer(f'this is /help',
                         reply_markup=kb.main)

@router.message(Command('settings'))
async def get_help(message:Message):
    await message.answer(f'this is /settings',
                         reply_markup=kb.settings)

@router.message(Command('cars'))
async def cars(message:Message):
     cars=["tesla","mercedes","BMW"]
     await message.answer(text="select cars",
                          reply_markup=await kb.reply_keyboard(cars))

@router.message(Command('car'))
async def car(message:Message):
     cars={"tesla":"https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM","mercedes":"https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM","BMW":"https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM"}
     await message.answer(text="select cars",
                          reply_markup=await kb.inline_keyboard(cars))

@router.message(F.text =='how are you?')
async def how_are_you(message:Message):
    await message.answer("ok!")

@router.message(Command('get'))
async def photo_reply(message:Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIBpmaBOGoYp7Y0YoDjB1n6m1Ux9yxZAAPYMRtNoghIjQqRjAULz0QBAAMCAAN5AAM1BA")


@router.message(Command('meme'))
async def meme(message:Message):
     
        url = 'https://api.imgflip.com/get_memes'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            memes = data['data']['memes']
            import random
            random_meme = random.choice(memes)
            print(f"Meme: {random_meme['name']}")
            print(f"URL: {random_meme['url']}")
            await message.answer_photo(
                 photo=random_meme['url'],
                 caption=random_meme['name']
            )
        else:
            print(f"Error: {response.status_code}")

@router.message(F.photo)
async def photo_re(message:Message):
        await message.answer(f'photo id is {message.photo[-1].file_id}')

@router.callback_query(F.data=='moshina')
async def moshina(callback:CallbackQuery):
    cars={"tesla":"https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM","mercedes":"https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM","BMW":"https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM"}
    
    await callback.answer('')
    await callback.message.edit_text(text="moshinala",
                                 reply_markup=await kb.inline_keyboard(cars))

@router.message(Command('reg'))
async def reg_one(message: Message,state: FSMContext):
     await state.set_state(Reg.name)
     await message.answer("enter your name!")


@router.message(Reg.name)
async def reg_two(message: Message,state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(Reg.number)
    await message.answer("enter your number")

@router.message(Reg.number)
async def reg_three(message:Message,state:FSMContext):
     await state.update_data(number=message.text)
     data= await state.get_data()
     await message.answer(f'thanks name:{data["name"]}\nnumber:{data["number"]}')
     await state.clear()