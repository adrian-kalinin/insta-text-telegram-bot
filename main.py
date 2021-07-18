from telegram.ext import Updater
import logging

import settings

from bot.models import database, User, Source
from bot.callbacks import error_callback

from bot.handlers import (
    start_handler, admin_handler,
    statistics_handler, backup_handler, mailing_conversation_handler,
    font_request_handler, font_translate_handler, back_handler,
    antispam_request_handler, antispam_translate_handler
)


# set up logger
logging.basicConfig(
    format='%(asctime)s – %(levelname)s – %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)


# create updater
updater = Updater(settings.BOT_TOKEN)
dispatcher = updater.dispatcher


# bound handlers to dispatcher
def bound_handlers():
    # noinspection PyTypeChecker
    dispatcher.add_error_handler(error_callback)

    # command handlers
    dispatcher.add_handler(admin_handler)
    dispatcher.add_handler(start_handler)

    # admin handlers
    dispatcher.add_handler(statistics_handler)
    dispatcher.add_handler(backup_handler)

    # mailing handlers
    dispatcher.add_handler(mailing_conversation_handler)

    # core handlers
    dispatcher.add_handler(back_handler)
    dispatcher.add_handler(font_request_handler)
    dispatcher.add_handler(font_translate_handler)
    dispatcher.add_handler(antispam_request_handler)
    dispatcher.add_handler(antispam_translate_handler)


# set up database
def configure_database():
    database.connect()
    database.create_tables([User, Source])
    database.close()
    logging.info('Database has been configured')


def main():
    # setting up application
    bound_handlers()
    configure_database()

    # setting up webhook
    updater.start_webhook(
        listen=settings.LISTEN,
        port=settings.PORT,
        url_path=settings.BOT_TOKEN,
        key=settings.KEY_PATH,
        cert=settings.CERT_PATH,
        webhook_url=settings.WEBHOOK_URL.format(
            host=settings.HOST,
            port=settings.PORT,
            token=settings.BOT_TOKEN
        )
    )

    # start bot
    updater.start_polling()
    logging.info('Bot has started')


if __name__ == '__main__':
    main()
