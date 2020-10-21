from django.shortcuts import render
# from django.contrib.auth import models as User
from apps.users import serializer as my_serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import generics, status, views, viewsets
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext_lazy as _
from apps.users import models
import random
import string 
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

class LoginView(generics.CreateAPIView):
    serializer_class = my_serializer.LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            session_key = ''

            session_key = session_key.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(64))
            existing_session = models.Session.objects.filter(user_id=user).exists()
            if existing_session:
                models.Session.objects.filter(user_id=user).update( session_key = session_key)
            else:
                new_session = models.Session(
			    session_key = session_key,
			    user = user,
			    )
                new_session.save()
            token = models.Session.objects.filter(user_id=user).get()
            data={}
            data['session'] = token.session_key
            return Response(data)
        else:
            try:
                found_user = User.objects.filter(email=email)
                if(found_user[0].is_active):
                    return Response({_("contaseña invalida.")}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({_("The user has not been activated.")}, status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response({_("No existe el usuario.")}, status=status.HTTP_401_UNAUTHORIZED)