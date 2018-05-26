from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    '''
    A class that defines the profile blueprint of the User
    '''
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    name = models.CharField(max_length =30,null=True)
    # estate = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
