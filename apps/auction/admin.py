from django.contrib import admin
from apps.auction import models
# Register your models here.

admin.site.register(models.Vehicle_in_auction)
admin.site.register(models.Offers)
admin.site.register(models.Vehicle_sold)