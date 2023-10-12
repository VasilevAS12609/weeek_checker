import os
from pathlib import Path
import logging
from telegram import (
    Bot,
    Update,
    KeyboardButton,
    MenuButtonCommands,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Defaults,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters,
)

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
path = os.path.dirname(BASE_DIR)
load_dotenv(path + '/infra/.env')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ALEXEY_ID = os.getenv('ALEXEY_ID')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def handle(self, *args, **kwargs):
    btn_1 = KeyboardButton('Сделать рассылку \u270D\uFE0F')

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_tg = update.message.chat.id
        first_name = update.message.chat.first_name
        last_name = update.message.chat.last_name
        markup = ReplyKeyboardMarkup(
            [
                [btn_1],
            ],
            resize_keyboard=True,
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Привет, {}. Я уже кое что умею \U0001F60E'.format(
                first_name),
            reply_markup=markup,
        )

    def main():
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

        start_handler = CommandHandler('start', start)

        application.add_handler(start_handler)

        application.run_polling()

    main()
