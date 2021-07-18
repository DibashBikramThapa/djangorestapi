from django.contrib import admin
from profileapp import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
