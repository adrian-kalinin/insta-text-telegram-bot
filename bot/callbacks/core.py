from telegram import Update
from telegram.ext import CallbackContext
import logging

from ..utils.dictionary import dictionary, antispam
from ..constants import Message, Keyboard
from ..models import User


def font_request_callback(update: Update, context: CallbackContext):
    from main import dispatcher

    user_data = dispatcher.user_data[update.effective_user.id]
    user_data['font'] = update.effective_message.text

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.send_text,
        reply_markup=Keyboard.back
    )


def font_translate_callback(update: Update, context: CallbackContext):
    from main import dispatcher

    user_data = dispatcher.user_data[update.effective_user.id]

    if font := user_data.get('font'):
        query = User.update(requests=User.requests + 1).where(User.user_id == update.effective_user.id)
        query.execute()

        logging.info(f'User {update.effective_user.id} made a request')

        text = update.effective_message.text
        translated = text.translate(dictionary[font])

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=translated
        )


def back_callback(update: Update, context: CallbackContext):
    from main import dispatcher

    dispatcher.user_data[update.effective_user.id].clear()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.back_to_menu,
        reply_markup=Keyboard.main
    )


def antispam_request_callback(update: Update, context: CallbackContext):
    from main import dispatcher

    user_data = dispatcher.user_data[update.effective_user.id]
    user_data[update.effective_message.text] = True

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.antispam,
        reply_markup=Keyboard.back
    )


def antispam_translate_callback(update: Update, context: CallbackContext):
    query = User.update(requests=User.requests + 1).where(User.user_id == update.effective_user.id)
    query.execute()

    logging.info(f'User {update.effective_user.id} made a request')

    text = update.effective_message.text.translate(antispam)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )
