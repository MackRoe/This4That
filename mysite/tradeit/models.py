import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class Offer(models.Model):
    offer_maker = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    offer_title = models.CharField(max_length=200)
    offer_description = models.TextField()
    tokens_requested = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.offer_title
