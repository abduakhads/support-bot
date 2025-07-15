import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.filters import Command

import cfg

dp = Dispatcher()


@dp.message(Command("start"))
async def startcmd(message: types.Message):
    await message.answer(
        "Hi, you can contact me via this bot, just send me your message"
    )


@dp.message()
async def mess(message: types.Message, bot: Bot):
    if message.from_user.id == int(cfg.SUPPORT):
        if not message.reply_to_message:
            return
        atr = message.reply_to_message.text.split("_")
        await message.copy_to(atr[1], reply_to_message_id=atr[0])
        return
    mess_id = (await message.forward(int(cfg.SUPPORT))).message_id
    await bot.send_message(
        int(cfg.SUPPORT),
        f"{message.message_id}_{message.from_user.id}_\n\nReply",
        reply_to_message_id=mess_id,
    )


async def main() -> None:
    bot = Bot(token=cfg.BOT_TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, handle_signals=True)


@dp.startup()
async def start_bot():
    print("Online")


if __name__ == "__main__":
    asyncio.run(main())
