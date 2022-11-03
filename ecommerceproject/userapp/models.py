from django.db import models

# Create your models here.
from statistics import mode
from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin)
from .managers import CustomUserManager
# from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractBaseUser):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=255)
    confirmpassword= models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    objects=CustomUserManager()
    
    class Meta:
        ordering = ('-created_at',)

    
    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    
    def __str__(self):
        return f'{self.username}|{self.email}'
    
   

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token)
