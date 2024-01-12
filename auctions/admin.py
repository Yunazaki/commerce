from django.contrib import admin
from .models import User, Auctions, Bids, Comments

class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'bid')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id')

class BidsAdmin(admin.ModelAdmin):
    list_display = ('bidder', 'auction', 'amount')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'auction')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Auctions, AuctionsAdmin)
admin.site.register(Bids, BidsAdmin)
admin.site.register(Comments, CommentsAdmin)