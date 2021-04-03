from django.contrib import admin
from myCard.models import UserProfile
from myCard.models import Card


admin.site.register(Card)
admin.site.register(UserProfile)
