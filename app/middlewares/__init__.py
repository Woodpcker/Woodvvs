from aiogram import Dispatcher

import logging

from .throttling import ThrottlingMiddleware, rate_limit

__all__ = ['setup_middleware', 'rate_limit']


def setup_middleware(dispatcher: Dispatcher):
    dispatcher.middleware.setup(ThrottlingMiddleware(limit=1))

    logging.info("Middleware are successfully configured")
