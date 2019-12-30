import datetime

from django.db import models

class Post(models.Model):
    tagline  = models.CharField(max_length=200, default="Lorem ipsum")
    content  = models.CharField(max_length=4000)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.content
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)