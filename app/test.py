
import asyncio

from aiogram import  F, Router, types
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,CallbackQuery

from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
from app.questions import questions as qt
import requests
import app.keyboards as kb

class Reg1(StatesGroup):
     name=State()
     number=State()
     test=State()
     end=State()
     score=State()

router1=Router()
@router1.message(Command('test'))
async def reg_test(message: Message,state: FSMContext):
     
     await state.update_data(score=0)
     await state.update_data(attempt=0)
     await message.answer("button bosing",
                          reply_markup=kb.test_inline)


@router1.callback_query(F.data=='start_test')
async def start_test(callback:CallbackQuery,state:FSMContext):
    result=await check_mark(callback,state)
    if not result:
          question,choices=qt()
          await callback.message.edit_text(question[1],
                                           reply_markup=await kb.inline_keyboard(choices))
    else:
         await callback.message.edit_text("Savollar tugadi ",
                                             reply_markup=kb.result)
     

async def increase_mark(state:FSMContext):
      data = await state.get_data()
       # Initialize score if it does not exist
      score = data['score'] +1
      print("increment ",score )
      await state.update_data(score=score)
      

async def check_mark(callback:CallbackQuery,state:FSMContext):
     data = await state.get_data()
     print("questions")
       # Initialize score if it does not exist
     attempt =data['attempt'] + 1
     print("questions", attempt)
     await state.update_data(attempt=attempt)
     return await check_attempts(callback,attempt)
           
async def check_attempts(callback:CallbackQuery,attempt):
     if attempt>50:
               return True
     else:
          False



@router1.callback_query(F.data=='true_answer') 
async def answer_true(callback:CallbackQuery,state:FSMContext):
     await increase_mark(state)
     
     await callback.message.edit_text(
               text="tog'ri javob",
               reply_markup=kb.next
          ) 
     
     
     

@router1.callback_query(F.data=='false_answer') 
async def answer_false(callback:CallbackQuery,state:FSMContext):
     await callback.message.edit_text(
               text="Notog'ri javob",
               reply_markup=kb.next
          )


@router1.callback_query(F.data=='end_test')
async def end_test(callback:CallbackQuery,state:FSMContext):
    
    data=await state.get_data()
    await callback.message.edit_text(f"To'g'ri topilgan savollar soni {data['score']} ta\nYana test yechish uchun /test bosin",)

    await state.clear()
    


     