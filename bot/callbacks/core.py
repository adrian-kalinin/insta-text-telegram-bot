from telegram import Update
from telegram.ext import CallbackContext
import logging

from ..utils.translator import dictionary, antispam, translate_instagram
from ..constants import Message, Keyboard
from ..models import User


def log_request(user_id):
    query = User.update(requests=User.requests + 1).where(User.user_id == user_id)
    query.execute()

    logging.info(f'User {user_id} made a request')


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
        log_request(update.effective_user.id)

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
    log_request(update.effective_user.id)

    text = update.effective_message.text.translate(antispam)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


def instagram_request_callback(update: Update, context: CallbackContext):
    from main import dispatcher

    user_data = dispatcher.user_data[update.effective_user.id]
    user_data[update.effective_message.text] = True

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.instagram,
        reply_markup=Keyboard.back
    )


def instagram_translate_callback(update: Update, context: CallbackContext):
    log_request(update.effective_user.id)

    text = translate_instagram(update.effective_message.text)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )
