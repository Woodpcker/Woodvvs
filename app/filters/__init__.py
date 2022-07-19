from .filters import IsPrivate, IsAdmin, IsAdminCall
from aiogram import Dispatcher

import logging


def setup_filters(dp: Dispatcher):
	dp.bind_filter(IsPrivate)
	dp.bind_filter(IsAdmin)
	dp.bind_filter(IsAdminCall)

	logging.info("Filters are successfully configured")


__all__ = ['setup_filters']
