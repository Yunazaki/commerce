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
    bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_listed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Bids(models.Model):
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="bids", default=0)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Bid #{self.id} on {self.auction.title} by {self.bidder.username}"


class Comments(models.Model):
    auction = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="comments", default=0)
    comment = models.CharField(max_length=255, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, default=0)