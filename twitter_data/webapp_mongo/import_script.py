#import_script.py  to extract the data according to the keywords list, and add the data to the model.

import logging
logging.basicConfig(filename='importscript.log',
                            filemode='w',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(lineno)d %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.info("Running Urban Planning")



import os,sys
from birdy.twitter import StreamClient


from mongoengine import *
connect('live-data')

from models import TwitterData
from requests.exceptions import ChunkedEncodingError,ConnectionError


def get_live_data():

    #twitter app COSUMER KEY,COSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
    CONSUMER_KEY = 'SQBP5hqu3KFAoA8V8kIYvz0ko'
    CONSUMER_SECRET = 'Do4XrWlZmz4d8thD2ZYXdcyDG0pWf1U4c8mi6ol7t8ZRBeGfhi'
    ACCESS_TOKEN = '151356238-WXtfWUZphySy0Em9qizCozVJA9FVue66Pfe2u2Xo'
    ACCESS_TOKEN_SECRET = 'f1Rd6IeEJDanFPcKAB6kPd09FdBbl1XrDMSvbFzPfTghb'

    client = StreamClient(CONSUMER_KEY,
                          CONSUMER_SECRET,
                          ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)


    keywords = ['technology','india','investing','india']

    while True:
        try:
            for keyword in keywords:
                resource = client.stream.statuses.filter.post(track=keyword)

                for data in resource.stream():
                    if 'text' in data:
                        tweets = TwitterData(tag=keyword, tweet_content=data['text'])
                        tweets.save()

                    else:
                        continue

        except (ChunkedEncodingError, ConnectionError, Exception):
            logger.error(Exception)
            continue



# get_live_data()






