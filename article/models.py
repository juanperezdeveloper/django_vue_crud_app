'''
@ Author: BrightStar1120
@ Date: 2019-03-24
@ Last Modified by: BrightStar1120
@ Last Modified Date: 2019-03-24
'''

from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()