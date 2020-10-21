from django.apps import AppConfig
from rest_framework import serializers
from apps.users import models 
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        elif user and not(user.is_active):
            raise serializers.ValidationError(_("The user has not been activated."))
        raise serializers.ValidationError(_("Unable to log in with provided credentials."))

class TokenCookieSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    cookie = serializers.CharField(max_length=255)
    session = serializers.CharField(max_length=255)
