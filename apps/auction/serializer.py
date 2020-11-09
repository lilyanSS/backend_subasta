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


class CreateOfferSerializer(serializers.Serializer):
    session = serializers.CharField()
    price_offered= serializers.FloatField()
    id_vehicle = serializers.IntegerField()
    user = serializers.IntegerField()

    def save(self):
        data = {}
        
        if self.is_valid():
            try:
                user_session = model_user.Session.objects.filter(session_key= self.validated_data['session']).get()
            except:
                raise serializers.ValidationError({'Error': 'Sesión de usuario inválida'})

        existing_vehicle = model_auction.Vehicle_in_auction.objects.get(id_vehicle= self.validated_data['id_vehicle'] ,on_sale=True )
        get_out_account= model_user.BankAccount.objects.get(user = self.validated_data['user'] )
        existing_offer=model_auction.Offers.objects.filter(user = self.validated_data['user'] ,id_vehicle= self.validated_data['id_vehicle']).exists()
        print('existing_offer  ->>>', existing_offer)
        print("cuenta usuario", get_out_account.total )
        if existing_offer:
            raise serializers.ValidationError({'Error': 'Ya tienes agregado este carro para el dia de la subasta'})
        else:
            print("Precio base del carro",existing_vehicle.base_price)
            if  self.validated_data['price_offered'] > get_out_account.total:
                raise serializers.ValidationError({'Error': 'No cuentas con suficiente presupuesto para  hacer la oferta.'})
            if existing_vehicle.base_price < self.validated_data['price_offered']:
                data = model_auction.Offers(
                    price_offered = self.validated_data['price_offered'],
                    id_vehicle = self.validated_data['id_vehicle'],
                    user = user_session.user,
                )
                data.save()
            else:
                raise serializers.ValidationError({'Error': 'El precio ofrecido es menor al precio base'})
        
        return data
