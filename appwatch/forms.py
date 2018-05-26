from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
#  Neighborhood,Post,Business,


class ProfileForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to update profile
    '''
    class Meta:
        model = Profile
        fields = ['profile_photo','name']