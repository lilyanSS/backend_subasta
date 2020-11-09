from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action,permission_classes
import json 
from rest_framework.response import Response
from apps.auction import serializer as my_serializer
from rest_framework.decorators import api_view 
from apps.users import models as models_user
from apps.auction import models as models_auction
import requests
User = get_user_model()

@api_view(['POST'],)
@permission_classes((AllowAny,))
def vechicleAuctionView(request):
    serializer = my_serializer.VehicleAuctionSerializer(data=request.data)
    data={}
    error={}
    if serializer.is_valid():
        new_data = serializer.save()
        data['msg'] = "Agregado exitosamente"
    else:
        error= serializer.errors
    context = {'data':data, 'error': error}
    print(context, " context")
    return Response(context)
 
@api_view(['GET'],)
@permission_classes((AllowAny,))
def auctionList(request):
    lists = models_auction.Vehicle_in_auction.objects.all()
    info=[]

    response = requests.get('http://lilyansica.pythonanywhere.com/vehicles/vehicles/');
    if response.status_code == 200:
        data= response.json()
        vehicles = data.get('results')
        for item in vehicles:
            for vehicle in lists:
                if(item['id'] == vehicle.id_vehicle):
                    info.append({
                        "id":vehicle.id,
                        "base_price":vehicle.base_price,
                        "creation_date":vehicle.creation_date,
                        "on_sale":vehicle.on_sale,
                        "id_vehicle":vehicle.id_vehicle,
                        "id_admin":vehicle.admin.id,                       
                        "car":item,
                        "auction_date":vehicle.auction_date
                    })

    return Response(info) 

@api_view(['POST'], )
@permission_classes((AllowAny,))
def vehicle_by_id(request):
    print(request.data["id"], "id")
    url = "http://lilyansica.pythonanywhere.com/vehicles/vehicles/{id}".format(id=request.data["id"])
    response = requests.get(url);

    if response.status_code ==200:
        data =response.json()
    else:
        data=[]
    return Response(data)

@api_view(['POST'], )
@permission_classes((AllowAny,))
def CreateOffer(request):
    serializer = my_serializer.CreateOfferSerializer(data=request.data)
    data={}
    error={}

    if serializer.is_valid():
        new_data = serializer.save()
        data['msg'] = "Tu oferta a sido agregada exitosamente."
    else:
        error= serializer.errors
    context = {'data':data, 'error': error}

    return Response(context)
