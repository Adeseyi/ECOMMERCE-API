from django.shortcuts import render
import re
from turtle import update
from urllib import response
from xmlrpc import server
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book, Product, Categories, Cart
from .serializer import BookSerializer
from .serializer import ProductSerializer
from .serializer import CategoriesSerializer
from .serializer import CartSerializer
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import action
from django.contrib.auth.models import User
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = UserDetailsSerializer


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer       

   

# Create your views here.
