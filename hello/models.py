from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_publisher = models.BooleanField(default=False)

class StockTrade(models.Model):
    TRADE_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]
    
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    