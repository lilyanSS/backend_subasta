from django.db import models
from django import forms
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='Username', unique=True)
    email = models.EmailField(('email address'), unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    EXTRA_USER_FIELD = 'username'

    def __str__(self):
        return f'{self.email}'

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='session_appuser')
    session_key = models.CharField(max_length=64)
    session_id = models.CharField(max_length=200, blank=True, unique=True, default=uuid.uuid4)
    creation = models.DateTimeField(auto_now_add=True)

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    account_number= models.CharField(verbose_name="Account number", validators=[RegexValidator(r'^[0-9]{1,50}?$')], max_length=50)
    account_name= models.CharField(max_length=100, verbose_name="Account name")
    total= models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return f'{self.user}'