from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from app.config import Config


class IsPrivate(BoundFilter):
	async def check(self, message: types.Message):
		return str(message.chat.type) == str(types.ChatType.PRIVATE)


class IsAdmin(BoundFilter):
	async def check(self, message: types.Message):
		cf = Config()
		admin_list = await cf.get_config('admins')
		return message.from_user.id in admin_list


class IsAdminCall(BoundFilter):
	async def check(self, call: types.CallbackQuery):
		cf = Config()
		admin_list = await cf.get_config('admins')
		return call.from_user.id in admin_list
