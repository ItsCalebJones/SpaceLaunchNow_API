import logging

from pyfcm import FCMNotification

from bot.app.buffer import BufferAPI
from spacelaunchnow.config import keys
from spacelaunchnow import config

logger = logging.getLogger('bot.notifications')


class NewsNotificationHandler:

    def __init__(self, debug=None):
        if debug is None:
            self.DEBUG = config.DEBUG
        else:
            self.DEBUG = debug
        self.buffer = BufferAPI()

    def send_notification(self, news):
        data = {"notification_type": 'featured_news',
                "click_action": "FLUTTER_NOTIFICATION_CLICK",
                "item": {
                    "id": news.id,
                    "news_site_long": news.news_site,
                    "title": news.title,
                    "url": news.link,
                    "featured_image": news.featured_image
                }}

        if not self.DEBUG:
            topics = "'prod_v2' in topics && 'featured_news' in topics"
            flutter_topics = "'flutter_production_v2' in topics && 'featured_news' in topics"
        else:
            topics = "'debug_v2' in topics && 'featured_news' in topics"
            flutter_topics = "'flutter_debug_v2' in topics && 'featured_news' in topics"

        push_service = FCMNotification(api_key=keys['FCM_KEY'])

        logger.info('----------------------------------------------------------')
        logger.info('Sending News notification - %s' % news.title)
        try:
            logger.info('News Notification Data - %s' % data)
            logger.info('Topics - %s' % topics)
            android_result = push_service.notify_topic_subscribers(data_message=data,
                                                                   condition=topics,
                                                                   time_to_live=86400, )
            logger.info(android_result)
        except Exception as e:
            logger.error(e)

        logger.info('----------------------------------------------------------')

        logger.info('----------------------------------------------------------')
        logger.info('Sending News Flutter notification - %s' % news.title)
        try:
            logger.info('News Notification Data - %s' % data)
            logger.info('Topics - %s' % flutter_topics)
            flutter_results = push_service.notify_topic_subscribers(data_message=data,
                                                                    condition=flutter_topics,
                                                                    time_to_live=86400,
                                                                    message_title="New article via " + data['item'][
                                                                        'news_site_long'],
                                                                    message_body=data['item']['title']
                                                                    )
            logger.info(flutter_results)
        except Exception as e:
            logger.error(e)

        logger.info('----------------------------------------------------------')

    def send_to_social(self, news_item):
        logger.info('Sending News ID:%s to Buffer!', news_item.id)
        if news_item.link:
            logger.info(self.buffer.send_to_twitter(message=news_item.title, link=news_item.link, now=True))
            logger.info(self.buffer.send_to_facebook(message=news_item.title, link=news_item.link, now=True))
            logger.info('Sent to Buffer!')
