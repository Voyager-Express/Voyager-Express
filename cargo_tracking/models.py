from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


## Custom User Model 
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault("role", "BASEADMIN")

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True')
    
        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('Email Adresi Boş Olamaz'))
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50, blank=True, editable=True)
    last_name = models.CharField(max_length=40, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=11, blank=True, unique=True, null=True)
    address = models.CharField(max_length=250, blank=True)
    role = models.CharField(max_length=15)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name


## Cargo Model    
class Cargo(models.Model):
    cargo_name = models.CharField(max_length=100) 
    ## bu alan göndericinin ve alıcının da hesapları olabileceği için yeniden düzenlenmiştir
    sender_customer_id = models.IntegerField(null= True)
    sender_first_name = models.CharField(max_length=50)
    sender_last_name = models.CharField(max_length=40)
    sender_address = models.CharField(max_length=250)
    sender_city = models.CharField(max_length=40)
    sender_phone = models.CharField(max_length=11, null=False)
    ## bu alan göndericinin ve alıcının da hesapları olabileceği için yeniden düzenlenmiştir
    reciever_customer_id = models.IntegerField(null= True)
    reciever_first_name = models.CharField(max_length=50)
    reciever_last_name = models.CharField(max_length=40)
    reciever_address = models.CharField(max_length=250)
    reciever_city = models.CharField(max_length=40)
    reciever_phone = models.CharField(max_length=11, null=False)
    cargo_type = models.CharField(max_length=50, blank=True, null=True)
    cargo_feature= models.CharField(max_length=50, blank=True, null=True)
    cargo_edt = models.CharField(max_length=50, blank=True, null=True)
    delivery_date = models.DateTimeField()
    courier_id = models.IntegerField()
    stage = models.IntegerField()

class Courier(models.Model):
    courier_id = models.BigIntegerField(primary_key=True)
    courier_name = models.CharField(max_length=80)
    cargo_limit = models.IntegerField(null=True)
    active_cargo_count = models.IntegerField(null=True)
    city = models.CharField(max_length=30, null=True)

class Cities(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=40)