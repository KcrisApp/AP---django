from django import forms
from django.contrib.auth.forms import UserChangeForm #Custom user
from .models import CustomUser
from django_registration.forms import RegistrationForm
#Custom user

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserForm(RegistrationForm):


    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "name","company_role","department")
  