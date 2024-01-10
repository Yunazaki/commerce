from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Auctions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(null=True, upload_to='media/')
    bid = models.FloatField(default=0)
    date_listed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass