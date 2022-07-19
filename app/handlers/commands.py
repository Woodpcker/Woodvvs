from aiogram import types

from app.db import *

import datetime


async def cmd_add(message: types.Message):
	data = message.text.split(' ')

	date = datetime.date.today()

	db = Database()
	await db.create_user(str(date), data[1], int(data[2]), data[3], message.from_user.username)

	await message.answer(
		'Done!'
	)


async def cmd_s(message: types.Message):
	data = message.text.split(' ')

	db = Database()
	user_data = await db.get_user(data[1])

	text = ''

	for i in user_data:
		text += ' | '.join(i) + '\n'

	if text == '':
		text = 'Ничего не найдено!'

	await message.answer(
		text
	)


async def cmd_dav(message: types.Message):
	db = Database()
	users_data = await db.get_users()

	text = ''

	for i in users_data:
		if i[2] != '0':
			text += ' | '.join(i) + '\n'

	if text == '':
		text = 'Ничего не найдено!'

	await message.answer(
		text
	)
