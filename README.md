# twitter-livestream

Twitter real time API to filter the tweets


This project deals with the twitter real time data API to extract the tweets and analyse them on hourly, weekly basis.

## Details and procedure regarding the Repo 

FrameWork Used: Django 1.11.

Database : MongoDB.

Languages : Python 2.7.


## Procedure

- [birdy-twiiter](https://github.com/inueni/birdy) to Stream the real time data from twitter.

- Created model, with the field tag and tweet_content and added the added tweets data to mongodb database.

- [django-crontab](https://pypi.python.org/pypi/django-crontab) to track the of real time data per hourly,weekly etc basis. 

