import logging
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
API_TOKEN = '6114909135:AAHT9Du5tQg1KFyUKyegBQ9el0diUfzlAFI'
# webhook settings
WEBHOOK_HOST = 'https://www.example.com/6114909135:AAHT9Du5tQg1KFyUKyegBQ9el0diUfzlAFI'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
# webserver settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)
    SendMessage(message.chat.id, message.text)
@dp.message_handler()
async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
@dp.message_handler()
async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')
if __name__ == '__main__':
    start_webhook(dispatcher=dp,webhook_path=WEBHOOK_PATH,on_startup=on_startup,on_shutdown=on_shutdown,skip_updates=True,host=WEBAPP_HOST,port=WEBAPP_PORT,)