from django.contrib import admin
from .models import User, Auctions, Bids

class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bid')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id')

class BidsAdmin(admin.ModelAdmin):
    list_display = ('bidder', 'auction', 'amount')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Auctions, AuctionsAdmin)
admin.site.register(Bids, BidsAdmin)