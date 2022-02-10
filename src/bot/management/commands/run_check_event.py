import datetime

import pytz
from api.models import Events
from celery.utils.log import get_task_logger
from django.core.management import BaseCommand

from bot.app.events.notification_handler import EventNotificationHandler

logger = get_task_logger("bot.events")

TAG = "Digest Server"


class Command(BaseCommand):
    help = "Run send Event manually."

    def add_arguments(self, parser):
        parser.add_argument("-debug", dest="debug", type=bool, const=True, nargs="?")

    def handle(self, *args, **options):
        logger.info("Check Events")
        event = Events.objects.filter(
            date__gte=datetime.datetime.now(tz=pytz.utc)
        ).first()
        if event:
            notification = EventNotificationHandler()
            notification.send_webcast_notification(event)
            # twitter = EventTwitterHandler()
            # twitter.send_ten_minute_tweet(event)
