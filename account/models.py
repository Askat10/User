from django.db import models
from django.contrib.auth.base_user import  BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
          

class ProfileChoices(models.TextChoices):
    customer = 'customer'     
    employee = 'employee'
    business = 'business'




class User(AbstractUser):
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField('Group')
    user_permissions = models.ManyToManyField('Permission')
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    profile = models.CharField(max_length=9, choices=ProfileChoices.choices, default='customer')
    username = None
    email = models.EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Group(models.Model):
    name = models.CharField(max_length=100)

class Permission(models.Model):
    pass