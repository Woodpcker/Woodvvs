from aiogram import Dispatcher, types
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled


def rate_limit(limit: int, key=None):
    """
    Decorator for configuring rate limit and key in different functions.
    :param limit:
    :param key:
    :return:
    """

    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        if key:
            setattr(func, "throttling_key", key)
        return func

    return decorator


class ThrottlingMiddleware(BaseMiddleware):
    """
    Simple middleware
    """

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix="antiflood_"):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        """
        This handler is called when dispatcher receives a message
        :param message:
        """
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()  # singletone
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(
                handler, "throttling_key", f"{self.prefix}_{handler.__name__}"
            )
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        """
        This handler is called when dispatcher receives a message
        :param message:
        """
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()  # singletone
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(
                handler, "throttling_key", f"{self.prefix}_{handler.__name__}"
            )
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(call.message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):
        """
        Notify user only on first exceed and notify about unlocking only on last exceed
        :param message:
        :param throttled:
        """
        # handler = current_handler.get()
        # dispatcher = Dispatcher.get_current()
        # if handler:
        #     key = getattr(
        #         handler, "throttling_key", f"{self.prefix}_{handler.__name__}"
        #     )
        # else:
        #     key = f"{self.prefix}_message"
        # # Calculate how many time is left till the block ends
        # delta = throttled.rate - throttled.delta
        # # Prevent flooding
        # if throttled.exceeded_count <= 3:
        #     await message.reply("<b>Вы были помещены в мут</b>")
        # print(delta, throttled.exceeded_count, key)
        # await asyncio.sleep(delta + 10)
        # thr = await dispatcher.check_key(key)
        # If current message is not last with current key - do not send message
        # if thr.exceeded_count == throttled.exceeded_count:
        #     await message.reply("<b>Разлокал.</b>")
        # handler = current_handler.get()
        # dispatcher = Dispatcher.get_current()
        # if handler:
        #     key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        # else:
        #     key = f"{self.prefix}_message"

        # # Calculate how many time is left till the block ends
        # delta = throttled.rate - throttled.delta

        # Prevent flooding
        if throttled.exceeded_count <= 2:
            await message.answer("Not so fast! Don't spam!")

        # Sleep.
        # await asyncio.sleep(delta)
        # Check lock status
        # thr = await dispatcher.check_key(key)

        # If current message is not last with current key - do not send message
        # if thr.exceeded_count == throttled.exceeded_count:
        #     await message.reply('Unlocked.')
