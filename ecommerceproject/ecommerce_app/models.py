import email
from email.headerregistry import Address
from email.policy import default
from enum import unique
from itertools import product
import profile
from venv import create
from django.db import models
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title



class Book(models.Model):
    title = models.CharField(max_length=250)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.CharField(max_length=1000)
    imageurl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title



class Product(models.Model):
    product_tag = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    stock = models.IntegerField()
    imageurl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        # return self.product_tag + "," + self.name
        return f"{self.product_tag}, {self.name}"


# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
#         now = timezone.now()
#         if not username:
#             raise ValueError("the given username is not valid")
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, is_active=False,
#                   is_staff=is_staff, is_superuser=is_superuser, date_joined=now, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_user(self, username, email, password, **extra_fields):
#         return self._create_user(username, email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields)

#     def create_superuser(self, username, email, password, **extra_fields):
#         user = self._create_user(username, email, password, is_active=True,
#                          is_staff=True, is_superuser=True, **extra_fields)
#         user.save(using=self._db)

#         return user  


# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=300, unique=True)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now())
#     receive_newsletter = models.BooleanField(default=False)
#     birth_date = models.DateTimeField(blank=True, null=True)
#     address = models.CharField(max_length=300, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     about_me = models.CharField(max_length=600, blank=True, null=True)
#     profile_image = models.ImageField(null=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email',]

class Cart(models.Model):
    cart_id = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)
    product = models.ManyToManyField(Product)

    # class Meta:
    #     ordering = ['cart_id', '-created_at']

    def _str_(self):
            return f'{self.cart}'    



       


          
# Create your models here.
