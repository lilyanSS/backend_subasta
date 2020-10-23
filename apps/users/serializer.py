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
            raise serializers.ValidationError(_("El usuario no ha sido activado."))
        raise serializers.ValidationError(_("No se puede iniciar la sesión con las credenciales proporcionadas."))

class PersonalInfo(serializers.Serializer):
    session = serializers.CharField()

    def to_representation(self, instance):
        data = super(PersonalInfo, self).to_representation(instance)
        info={}
        if self.is_valid():
            try:
                user_session = models.Session.objects.filter(session_key= self.validated_data['session']).get()
            except:
                raise serializers.ValidationError({'Error': 'Sesión de usuario inválida'})
        info['firstname']= user_session.user.first_name
        info['lastname']= user_session.user.last_name
        info['email']= user_session.user.email
        info['is_superuser'] = user_session.user.is_superuser
        info['date_joined'] = user_session.user.date_joined
        data.update(info)
        return data

class BankAccountInfo(serializers.Serializer):
    session = serializers.CharField()

    def to_representation(self, instance):
        data = {}
        info={}
        if self.is_valid():
            try:
                user_session = models.Session.objects.filter(session_key= self.validated_data['session']).get()
                bank_account= models.BankAccount.objects.filter(user=user_session.user).exists()
                if bank_account:
                    bank_account= models.BankAccount.objects.filter(user=user_session.user).get()
                    info["account_number"]=bank_account.account_number
                    info["account_name"]=bank_account.account_name
                    info["total"]=bank_account.total
            except:
                raise serializers.ValidationError({'Error': 'Sesión de usuario inválida'})
        data.update(info)
        return data


