from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Neighborhood
# ,Post,Business,


class ProfileForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to update profile
    '''
    class Meta:
        model = Profile
        fields = ['profile_photo','name']

class NeighborhoodForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create neighborhood
    '''
    class Meta:
        model = Neighborhood
        fields = ['neighborhood_name','neighborhood_location', 'population']