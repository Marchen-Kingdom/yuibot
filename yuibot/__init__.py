import os

import aiocqhttp
import nonebot
from nonebot import Message, MessageSegment, message_preprocessor
from nonebot.message import CanceledException

from . import config
from .log import new_logger

__version__ = "2.1.0"

_bot = None
YuiBot = nonebot.NoneBot
os.makedirs(os.path.expanduser("~/.yuibot"), exist_ok=True)
logger = new_logger("yuibot", config.DEBUG)


def init() -> YuiBot:
    global _bot
    nonebot.init(config)
    _bot = nonebot.get_bot()
    _bot.finish = _finish

    from .log import critical_handler, error_handler

    nonebot.logger.addHandler(error_handler)
    nonebot.logger.addHandler(critical_handler)

    for module_name in config.MODULES_ON:
        nonebot.load_plugins(
            os.path.join(os.path.dirname(__file__), "modules", module_name),
            f"yuibot.modules.{module_name}",
        )

    from . import msghandler

    return _bot


async def _finish(event, message, **kwargs):
    if message:
        await _bot.send(event, message, **kwargs)
    raise CanceledException("ServiceFunc of YuiBot finished.")


def get_bot() -> YuiBot:
    if _bot is None:
        raise ValueError("YuiBot has not been initialized")
    return _bot


def get_self_ids():
    return _bot._wsr_api_clients.keys()


from . import R
from .service import Service, sucmd
