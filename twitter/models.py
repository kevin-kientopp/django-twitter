from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweet(models.Model):
    body = models.CharField(max_length=140)
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.body
