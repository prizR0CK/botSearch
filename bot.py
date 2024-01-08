import asyncio
import logging
import sys
import search
from keyboard import keyBoard
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram import types
from config import TOKEN

dp = Dispatcher()

dp.include_routers(search.routing)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    logging.warning(message.from_user)
    await message.answer(f'Hallo {hbold(message.from_user.full_name)} !\n How are you?', reply_markup=keyBoard)


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
