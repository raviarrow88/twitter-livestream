#clean_duplicates.py removes the duplicate data on db updatation

from mongoengine import *
connect('live-data')

from models import TwitterData
from requests.exceptions import ChunkedEncodingError,ConnectionError





def clean_duplicate_data():
    for i, j in enumerate(TwitterData.objects):
        find_dupe = TwitterData.objects.filter(tweet_content=j.tweet_content)
        if find_dupe.count() > 1:
            find_dupe.delete()

