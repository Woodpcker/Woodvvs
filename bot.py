from aiogram import executor

from app import *


async def on_startup(dp):
	# await set_commands(dp)

	# setup_filters(dp)
	setup_middleware(dp)
	setup_handlers(dp)


if __name__ == '__main__':
	executor.start_polling(
		dispatcher=dp,
		skip_updates=False,
		on_startup=on_startup
	)
