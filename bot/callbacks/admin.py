from telegram import Update, ParseMode, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from peewee import fn
from datetime import datetime
import os

from settings import DATABASE_PATH

from ..models import User, Source
from ..constants import Message, States


def statistics_callback(update: Update, context: CallbackContext):
    total_users = User.select().count()
    active_users = User.select().where(User.active == True).count()
    total_requests = User.select(fn.sum(User.requests).alias('total')).dicts()[0].get('total')

    text = Message.statistics.format(
        total_users=total_users,
        active_users=active_users,
        total_requests=total_requests
    )

    context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id,
        text=text, parse_mode=ParseMode.HTML
    )

    text = Message.sources

    for source in Source.select():
        text += f'{source.name} — {source.users}\n'

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text, parse_mode=ParseMode.HTML
    )


def mailing_callback(update: Update, context: CallbackContext):
    context.bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=Message.mailing,
        reply_markup=ReplyKeyboardRemove()
    )

    return States.prepare_mailing


def backup_callback(update: Update, context: CallbackContext):
    date = datetime.today().strftime('%d.%m.%Y')

    context.bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id
    )

    if os.path.isfile(DATABASE_PATH):
        with open(DATABASE_PATH, 'rb') as file:
            context.bot.send_document(
                chat_id=update.effective_chat.id,
                caption=Message.backup.format(date),
                document=file
            )

    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=Message.database_not_found
        )
