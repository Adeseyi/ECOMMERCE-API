from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import User
from rest_framework import generics,status,views
from .serializers import RegistrationSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import permissions



# Create your views here.
class RegistrationView(views.APIView):
    serializer_class = RegistrationSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        user = User.objects.get(email=user_data['email'])
    #     refresh = RefreshToken.for_user(user)
    #     user_data['token']={
    #     'refresh': str(refresh),
    #     'access': str(refresh.access_token),
    # } 
        return Response(user_data,status=status.HTTP_201_CREATED)
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

