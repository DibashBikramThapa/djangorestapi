from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from profileapp.models import UserProfile
from django.contrib import auth

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("email","username", "password1", "password2")
        model = get_user_model()
 
