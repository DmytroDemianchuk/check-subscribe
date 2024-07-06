import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import config as cfg

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

async def check_sub_channels(channels, user_id):
       for channel in channels: 
              chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
              if chat_member['status'] == 'left':
                    return False
              return True


@dp. message_handler(commands=['start'])
async def start(message: types.Message):
        if message.chat.type == 'private':
                if await check_sub_channels(cfg.CHANNELS, message.from_user.id):
                    await bot.send_message(message.from_user.id, "Привіт!", reply_marcup=nav.profileKeyboard)
                else:
                    await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

@dp.message_handler()
async def bot_message(message: types.Message):
        if message.chat.type == 'private':
             if await check_sub_channels(cfg.CHANNELS, message.from_user.id):
                if message.text == "Профіль":
                   await bot.send_message(message.from_user.id, f"Ваш ID:{message.from_user.id}")
                else:
                        await bot.send_message(message.from_user.id, cfg.NOT_SUB_MESSAGE, reply_markup=nav.showChannels())

if __name__ == "__main__":
       executor.start_polling(dp, skip_updates = True)