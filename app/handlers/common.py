from aiogram import types

from app.db import *
from app.config import *
from app.middlewares import rate_limit


@rate_limit(5)
async def cmd_start(message: types.Message):
	await message.answer(
		'Бот работает'
	)
