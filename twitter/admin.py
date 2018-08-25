from django.contrib import admin
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    list_filter = ['auth_user']

admin.site.register(Tweet, TweetAdmin)
