from django.apps import AppConfig
from rest_framework import serializers
from apps.users import models as model_user
from apps.auction import models as model_auction 
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class VehicleAuctionSerializer(serializers.Serializer):
    session = serializers.CharField()
    base_price= serializers.FloatField()
    id_vehicle = serializers.IntegerField()
    auction_date =  serializers.DateField()

    def save(self):
        data = {}
        info={}
        if self.is_valid():
            try:
                user_session = model_user.Session.objects.filter(session_key= self.validated_data['session']).get()
                
               
            except:
                raise serializers.ValidationError({'Error': 'Sesión de usuario inválida'})

        existing_vehicle = model_auction.Vehicle_in_auction.objects.filter(id_vehicle= self.validated_data['id_vehicle'] ,on_sale=True ).exists()

        if existing_vehicle :
            raise serializers.ValidationError({'Error': 'El vehiculo ingresado ya esta registrado actualmente'})
        else:
            data = model_auction.Vehicle_in_auction(
                base_price = self.validated_data['base_price'],
                id_vehicle = self.validated_data['id_vehicle'],
                admin = user_session.user,
                auction_date = self.validated_data['auction_date']
                )
            data.save()

        return data

class AuctionListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = model_auction.Vehicle_in_auction
        fields ="__all__"  

