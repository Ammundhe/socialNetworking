from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from user_profile.models import UserProfile

class createAccountform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email']


class userProfileform(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_picture', 'mobile', 'address']

