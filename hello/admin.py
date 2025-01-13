from django.contrib import admin
from .models import UserProfile, StockTrade

admin.site.register(UserProfile)
admin.site.register(StockTrade)
