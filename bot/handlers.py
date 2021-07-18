from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters

from settings import ADMINS

from .filters import font_filter, antispam_filter, instagram_filter
from .constants import CallbackData, States, ReplyButtons
from .utils.translator import dictionary
from .callbacks import *


# command handlers
admin_handler = CommandHandler(
    command='admin', callback=admin_command_callback,
    filters=Filters.user(user_id=ADMINS)
)

start_handler = CommandHandler(
    command='start', callback=start_command_callback
)

# admin handlers
statistics_handler = CallbackQueryHandler(
    pattern=CallbackData.statistics,
    callback=statistics_callback
)

backup_handler = CallbackQueryHandler(
    pattern=CallbackData.backup,
    callback=backup_callback
)

# mailing handlers
mailing_conversation_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern=CallbackData.mailing, callback=mailing_callback)],
    states={
        States.prepare_mailing: [MessageHandler(callback=mailing_message_callback, filters=Filters.all)],
        States.received_mailing: [
            MessageHandler(filters=Filters.text(ReplyButtons.preview_mailing), callback=preview_mailing_callback),
            MessageHandler(filters=Filters.text(ReplyButtons.cancel_mailing), callback=cancel_mailing_callback),
            MessageHandler(filters=Filters.text(ReplyButtons.send_mailing), callback=send_mailing_callback)
        ]
    },
    fallbacks=[]
)

# core handlers
back_handler = MessageHandler(
    filters=Filters.text(ReplyButtons.back),
    callback=back_callback
)

font_request_handler = MessageHandler(
    filters=Filters.text(list(dictionary.keys())),
    callback=font_request_callback
)

font_translate_handler = MessageHandler(
    filters=Filters.text & font_filter,
    callback=font_translate_callback
)

antispam_request_handler = MessageHandler(
    filters=Filters.text(ReplyButtons.antispam),
    callback=antispam_request_callback
)

antispam_translate_handler = MessageHandler(
    filters=Filters.text & antispam_filter,
    callback=antispam_translate_callback
)

instagram_request_handler = MessageHandler(
    filters=Filters.text(ReplyButtons.instagram),
    callback=instagram_request_callback
)

instagram_translate_handler = MessageHandler(
    filters=Filters.text & instagram_filter,
    callback=instagram_translate_callback
)

