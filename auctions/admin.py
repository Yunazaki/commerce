from django.contrib import admin
from .models import User, Auctions

class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bid')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Auctions, AuctionsAdmin)