import requests
from aiogram.utils.markdown import hbold, hlink
from aiogram import F, types, Router

API = 'http://127.0.0.1:8000/api/search/'
status_code = 0


def goods_search(name, search_text):
    global status_code
    try:
        req_s = requests.post(API, data={'name': name, 'search_query': search_text})
        status_code = req_s.status_code
        return req_s.json()
    except Exception as e:
        print(e)
        status_code = 0


routing = Router()


@routing.message(F.text == 'Goods search')
async def cmd_search(message: types.Message):
    await message.answer("Write which product you would like to find")


@routing.message(F.text)
async def cmd_search_go(message: types.Message):
    name = message.from_user.full_name
    text = message.text
    await message.answer("just a second...")
    products = goods_search(name, text)
    if status_code == 200:
        for product in products:
            await message.answer(product.get('shop_name'))
            card = \
                f"{hbold(product.get('name'))}\n" \
                f"{hbold(product.get('price'))}\n" \
                f"{hlink('follow the link', product.get('link'))}\n" \

            await message.answer(card)
    elif status_code == 0:
        await message.answer("Failed to connect")
    else:
        await message.answer("Unfortunately cannot find")
