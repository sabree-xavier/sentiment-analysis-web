import datetime
from django.db import models
import pytz
from pytz import timezone


# Create your models here.
class ReviewModel(models.Model):
    review = models.CharField(max_length=1000)
    timestamp_field = models.DateTimeField()
    sentiment_value = models.IntegerField()
    user = models.CharField(max_length=50)
    
    def __str__(self):
        return self.review
    
class ResumeModel(models.Model):
    file = models.FileField(upload_to='documents')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name