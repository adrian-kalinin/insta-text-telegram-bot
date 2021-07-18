from telegram import Update
from telegram.ext import UpdateFilter

from .constants import ReplyButtons


class FontFilter(UpdateFilter):
    def filter(self, update: Update):
        from main import dispatcher

        user_data = dispatcher.user_data[update.effective_user.id]

        return user_data.get('font')


class AntispamFilter(UpdateFilter):
    def filter(self, update: Update):
        from main import dispatcher

        user_data = dispatcher.user_data[update.effective_user.id]

        return user_data.get(ReplyButtons.antispam)


font_filter = FontFilter()
antispam_filter = AntispamFilter()
