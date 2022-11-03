from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None,**other_fields):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email),**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password=None,**other_fields):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password,**other_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

