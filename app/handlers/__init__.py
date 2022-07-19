from .common import *
from .commands import *

from aiogram import Dispatcher

import logging

from app.filters import IsPrivate, IsAdmin

__all__ = ['setup_handlers']


def setup_handlers(dp: Dispatcher):
	dp.register_message_handler(cmd_start, IsPrivate(), commands='start', state='*')

	dp.register_message_handler(cmd_add, commands='add', state='*')
	dp.register_message_handler(cmd_s, commands='s', state='*')
	dp.register_message_handler(cmd_dav, commands='dav', state='*')

	logging.info("Handlers are successfully configured")
