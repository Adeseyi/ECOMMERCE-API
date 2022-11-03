from .models import User
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegistrationSerializer(serializers.ModelSerializer):
    confirmpassword= serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = fields = ["id",'email', 'username', 'password',"confirmpassword",'firstname','lastname','phoneno','is_verified','last_login','created_at']
        extra_kwargs ={
            'password': {'write_only': True,'min_length': 8},
            'last_login': {'read_only': True}
        }
        
    def save(self):
        password= self.validated_data['password']
        confirmpassword= self.validated_data['confirmpassword']

            
        if password  != confirmpassword:
                raise serializers.ValidationError({'error':'check your password again'})
            
        if User.objects.filter(email=self.validated_data['email']).exists():
                raise serializers.ValidationError({'error':'email already exists'})
            
        account =User(email=self.validated_data['email'],username= self.validated_data['username'])
        account.set_password(password)
        account.save()  
        return account
            
    
    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('invalid credentials')
        return {
            'email': user.email,
            'username': user.username,
            # 'tokens': user.tokens
        }
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
   
    
    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('invalid credentials')
        return {
            'email': user.email,
            'username': user.username,
        
        }
