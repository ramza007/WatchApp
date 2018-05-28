from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Neighborhood, Business ,Post


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

class PostBusinessForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to post a business
    '''
    class Meta:
        model = Business
        fields = ['cover_image','business_name', 'email']

class PostMessageForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to post a message
    '''
    class Meta:
        model = Post
        fields = ['image','image_name', 'message']