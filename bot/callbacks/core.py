from telegram import Update
from telegram.ext import CallbackContext

from ..constants import Message, Keyboard


def font_callback(update: Update, context: CallbackContext):
    context.user_data['font'] = update.effective_message.text

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.send_text,
        reply_markup=Keyboard.back
    )


def back_callback(update: Update, context: CallbackContext):
    context.user_data.clear()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.back_to_menu,
        reply_markup=Keyboard.main
    )
