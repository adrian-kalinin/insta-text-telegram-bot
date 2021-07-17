from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from itertools import islice

from .utils.dictionary import dictionary


def generate_main_buttons():
    iter_keys = iter(dictionary.keys())
    buttons = iter(lambda: list(islice(iter_keys, 2)), [])
    return list(buttons)


class States:
    prepare_mailing = 1
    received_mailing = 2


class CallbackData:
    statistics = 'statistics'
    mailing = 'mailing'
    backup = 'backup'


class ReplyButtons:
    send_mailing = 'Отправить'
    preview_mailing = 'Предпросмотр'
    cancel_mailing = 'Отмена'

    back = 'Назад'


class Keyboard:
    main = ReplyKeyboardMarkup([
        *generate_main_buttons()
    ], resize_keyboard=True)

    back = ReplyKeyboardMarkup([
        [ReplyButtons.back]
    ])

    admin = InlineKeyboardMarkup([
        [InlineKeyboardButton('Посмотреть статистику', callback_data=CallbackData.statistics)],
        [InlineKeyboardButton('Создать рассылку', callback_data=CallbackData.mailing)],
        [InlineKeyboardButton('Копировать базу данных', callback_data=CallbackData.backup)]
    ])

    mailing = ReplyKeyboardMarkup([
        [ReplyButtons.send_mailing],
        [ReplyButtons.preview_mailing, ReplyButtons.cancel_mailing]
    ], resize_keyboard=True)


class Message:
    start = 'Привет!'

    send_text = 'Пришлите текст для конвертации в выбранный шрифт'

    back_to_menu = 'Вы вернулись в главное меню'

    admin = 'Добро пожаловать в админскую панель!'

    statistics = (
        '✨ <b>Статистика бота</b> ✨\n\n'
        'Количество пользователей: <b>{total_users}</b>\n'
        'Из них активных: <b>{active_users}</b>\n\n'
        'Запросов за всё время: <b>{total_requests}</b>'
    )

    mailing = 'Отправьте сообщение для рассылки'

    received_mailing = 'Сообщение получено. Что дальше?'

    mailing_canceled = 'Рассылка отменена'

    mailing_started = 'Рассылка началась'

    mailing_finished = (
        'Сообщение отправлено успешно:\n\n'
        'Получившие пользователи: {sent_count}'
    )

    unexpected_error = '<code>Telegram Error: {error}.\n\n{update}</code>'

    backup = 'Бэкап базы данных ({})'

    database_not_found = 'База данных не найдена'
