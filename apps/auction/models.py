from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
# Create your models here.
class Vehicle_in_auction(models.Model):
    base_price = models.FloatField(verbose_name="base_price")
    creation_date = models.DateTimeField(default=timezone.now)
    on_sale = models.BooleanField(default=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    id_vehicle= models.IntegerField()




