from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

import logging

from app import Config


async def set_commands(dp: Dispatcher):
	commands = [
		BotCommand(command='/start', description='Start/reload bot'),
	]

	await dp.bot.set_my_commands(commands)
	logging.info('Standard commands are successfully configured')


logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

config = Config()

bot = Bot(
	token=config.get_config_sync('bot_token'),
	parse_mode=types.ParseMode.HTML
)

dp = Dispatcher(
	bot=bot,
	storage=MemoryStorage()
)
