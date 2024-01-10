from django.contrib import admin
from .models import User, Auctions

class AuctionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bid')

# Register your models here.
admin.site.register(User)
admin.site.register(Auctions, AuctionsAdmin)