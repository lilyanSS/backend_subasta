from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
# Create your models here.
class Vehicle_in_auction(models.Model):
    base_price = models.FloatField(verbose_name="base_price")
    creation_date = models.DateTimeField(default=timezone.now)
    auction_date =  models.DateField(null=True)
    on_sale = models.BooleanField(default=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    id_vehicle= models.IntegerField()

class Offers(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    creation_date = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=True)
    id_vehicle= models.IntegerField()
    price_offered= models.FloatField()
    vehicle_in_auction= models.ForeignKey(Vehicle_in_auction, on_delete=models.CASCADE, null=True) 


