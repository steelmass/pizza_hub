from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command, Text

import os
import asyncio
import logging


async def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - '
                               '%(message)s')

    load_dotenv()
    token = os.getenv('BOT_API')
    bot = Bot(token=token)
    dp = Dispatcher()

    @dp.message(Command(commands=['start']))
    async def start(msg: types.Message):
        await msg.answer('Hello')

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
