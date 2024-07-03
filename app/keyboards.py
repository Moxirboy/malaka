from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
main=ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="nima gap")
    ],
    [KeyboardButton(text="yaxshi"),KeyboardButton(text="yomon")]
    ],
    resize_keyboard=True
)

inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Moshinala",callback_data='moshina')],
        [InlineKeyboardButton(text="uyla",callback_data='moshina')],
        [InlineKeyboardButton(text="matrasla",callback_data='moshina')]

    ]
)
next=InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text="Keyingi savol",callback_data='start_test')],

    ]
)
result=InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text="resultatni bilish",callback_data='end_test')],

    ]
)
startbutton=InlineKeyboardMarkup(
    inline_keyboard=[
           [ InlineKeyboardButton(text="Testni boshlash", callback_data="start_test")
]
    ]
)

test_inline=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Test boshlash!",callback_data='start_test')],]
)


settings=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="tinchmi",url="https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM")],
        [InlineKeyboardButton(text="QALAY",url="https://youtu.be/qRyshRUA0xM?list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM")
         ]
    ]
)



async def reply_keyboard(cars):
    keyboard=InlineKeyboardBuilder()
    i=0
    for car in cars:
        if i == 0:
            keyboard.add(InlineKeyboardButton(text=car, callback_data='true_answer'))
            i+=1
        else:
            keyboard.add(InlineKeyboardButton(text=car, callback_data='false_answer'))
        
    return keyboard.adjust(3).as_markup()

import random
async def inline_keyboard(cars):
    buttons = []
    if not cars:
        buttons.append(InlineKeyboardButton(text="Javoblari yoq keyingi savolga o'tish", callback_data='start_test'))
    i=0
    for car in cars:
        if i == 0:
            buttons.append(InlineKeyboardButton(text=car, callback_data='true_answer'))
            i+=1
        else:
            buttons.append(InlineKeyboardButton(text=car, callback_data='false_answer'))
        
    random.shuffle(buttons)
    random.shuffle(buttons)
    
    keyboard=InlineKeyboardBuilder()
    for button in buttons:
        # print(button)
        keyboard.add(button)
    
    return keyboard.adjust(1).as_markup()
