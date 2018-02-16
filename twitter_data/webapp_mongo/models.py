# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from mongoengine import *


class TwitterData(Document):
    tag = StringField()
    tweet_content = StringField()

