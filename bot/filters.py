from telegram import Update
from telegram.ext import UpdateFilter

from .constants import ReplyButtons


def get_user_data(user_id):
    from main import dispatcher

    return dispatcher.user_data[user_id]


class FontFilter(UpdateFilter):
    def filter(self, update: Update):
        return get_user_data(update.effective_user.id).get('font')


class AntispamFilter(UpdateFilter):
    def filter(self, update: Update):
        return get_user_data(update.effective_user.id).get(ReplyButtons.antispam)


class InstagramFilter(UpdateFilter):
    def filter(self, update: Update):
        return get_user_data(update.effective_user.id).get(ReplyButtons.instagram)


font_filter = FontFilter()
antispam_filter = AntispamFilter()
instagram_filter = InstagramFilter()
