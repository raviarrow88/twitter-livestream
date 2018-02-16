# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tweet(models.Model):
    tag = models.CharField(max_length=100,blank=True,null=True,default=None)
    tweet_content = models.TextField(blank=True,null=True,default=None)


    def __str__(self):
        return "%s"%(self.tag)