from django.db import models
from django import forms
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='Username', unique=True)
    email = models.EmailField(('email address'), unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    EXTRA_FIELDS = ['id', 'birth_date', 'city_name', 'address', 'state', 'postal_code', 'photo', 'is_active', 'date_joined']
    EXTRA_USER_FIELD = 'username'

    def __str__(self):
        return f'{self.email}'

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='session_appuser')
    session_key = models.CharField(max_length=64)
    session_id = models.CharField(max_length=200, blank=True, unique=True, default=uuid.uuid4)
    creation = models.DateTimeField(auto_now_add=True)
