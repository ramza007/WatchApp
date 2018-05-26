from django.db import models
import datetime as dt
from django.contrib.auth.models import User


# Create your models here.

#-----------------Profile modules-------------#

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

#---------------------Neighbourhood modules-----------------#
class Neighborhood(models.Model):
    '''
    A class that defines the blueprint of a Neighborhood model
    '''
    neighborhood_name = models.CharField(max_length =30,null=True)
    neighborhood_location = models.CharField(max_length =30, null =True)
    population = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.neighborhood_name

    def create_neighborhood(self):
        '''
        Metuserhods that saves a new neighborhood
        '''
        self.save()

    def delete_neighborhood(self):
        '''
        Methods that deletes an exiting neighborhood
        '''
        self.delete()
    @classmethod
    def get_neighborhoods(cls):
        '''
        Methods that fetches all hoods
        '''
        estates = Neighborhood.objects.all()
        return estates
    @classmethod
    def get_specific_hood(cls,id):
        '''
        fetches particular hood in the exiting neighborhood
        '''
        chosen_hood = cls.objects.get(id=id)
        return chosen_hood

    def update_neighborhood(self):
        '''
        Methods that updates an exiting neighborhood
        '''
        pass

    def update_occupants(self):
        email = models.EmailField(max_length=70,blank=True)
        '''
        Methods that updates the population size
        '''

        pass

    @classmethod
    def find_neighbourhood(neigborhood_id):
        '''
        Method to search for a particular neighbourhood
        '''
        query = cls.objects.filter(name__icontains=search_term)
        return query