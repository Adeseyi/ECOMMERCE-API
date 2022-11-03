
from asyncore import write
from ctypes import addressof
from dataclasses import field, fields
from importlib.metadata import requires
from itertools import product
from sqlite3 import adapters
from urllib.request import Request
from rest_framework import serializers
from ecommerce_app.models import Product, Book, Categories
from .models import Cart
from django.conf import settings


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'imageurl', 'categories', 'isbn', 'pages', 'price', 'stock', 'status', 'description', 'date_created']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_tag', 'imageurl', 'categories', 'name', 'price', 'stock', 'status', 'date_created']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'title']



# class RegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
#     first_name = serializers.CharField(required=False, write_only=True)
#     lats_name = serializers.CharField(required=False, write_only=True)
#     address = serializers.CharField(required=False, write_only=True)

#     password1 = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)

#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)

#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(
#                 ("The two password fields didn't match"))
#         return data

#     def get_clearned_data(self):
#         return {
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', ''),
#             'address': self.validated_data.get('address', ''),
#             'user_type': self.validated_data.get('user_type', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#         }

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.clearned_data = self.get_clearned_data()
#         adapter.save_user(request, user, self)
#         self.custom_signup(Request, user)
#         setup_user_email(Request, user, [])
#         return user

#         user.save()
#         return user


# class UserDetailsSerializer(serializers.ModelSerializer):
#     """
#     User model w/o password
#     """                    
#     class Meta:
#         fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'address',
#                   'phone_number', 'country', 'city', 'about_me', 'profile_image'
#                   )
#         read_only_fields = ('email',)



class CartSerializer(serializers.ModelSerializer):

    books = BookSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'books', 'products')
                           

        


