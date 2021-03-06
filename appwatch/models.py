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



#------------Follow Module-------------#
class Follow(models.Model):
    '''
    Class that store a User and Profile follow neighborhood news
    '''
    user = models.ForeignKey(User)
    estate = models.ForeignKey(Neighborhood)


    def __str__(self):
        return self.user.username

    @classmethod
    def get_following(cls,user_id):
        following =  Follow.objects.filter(user=user_id).all()
        return following




#-----------------------------Business modules-----------------------#
class Business(models.Model):
    '''
    A class that defines the business blueprint
    '''
    cover_image = models.ImageField(upload_to = 'business/', null=True, blank=True)
    business_name = models.CharField(max_length =30,null=True)
    email =  models.EmailField(max_length=70,blank=True)
    estate = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.business_name

    @classmethod
    def get_specific_business(cls,id):
        '''
        fetches particular hooddeletes an exiting neighborhood
        '''
        business = cls.objects.filter(id=id)
        return business


    @classmethod
    def get_businesses(cls):
        '''
        fetches particular hooddeletes an exiting neighborhood
        '''
        business = cls.objects.all()
        return business

    @classmethod
    def get_business_by_estate(cls,hood_id):
        '''
        Method that gets all posts in a specific neighbourhood from the database
        Returns:
            messages : list of post objects from the database
        '''
        messages = cls.objects.all().filter(estate=hood_id)
        return messages

class Post(models.Model):
    '''
    A class that defines posts of the users
    '''
    image = models.ImageField(upload_to = 'photos/', null = True,blank=True,)
    image_name = models.CharField(max_length=30)
    message =models.TextField(max_length = 100, null =True,blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    estate = models.ForeignKey(Neighborhood,null =True,blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-date_uploaded']

    def save_post(self):
        '''
        Method to save an post in the database
        '''
        self.save()

    def delete_post(self):
        ''' Method to delete an post from the database'''
        self.delete()

    @classmethod
    def get_posts(cls):
        '''
        Method that gets all posts from the database
        Returns:
            messages : list of post objects from the database
        '''
        messages = cls.objects.all()
        return messages

    @classmethod
    def get_posts_by_estate(cls,hood_id):
        '''
        Method that gets all posts in a specific neighbourhood from the database
        Returns:
            messages : list of post objects from the database
        '''
        messages = cls.objects.all().filter(estate=hood_id)
        return messages
