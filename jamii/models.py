from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants = models.IntegerField(null=True, default=0)
    
    def __str__(self):
        return self.name
    
    def create_neighbourhood(self):
        self.save()
    
    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        neighbourhood = cls.objects.get(id = neighbourhood_id)
        return neighbourhood

    def update_neighbourhood(self):
        self.save()

    def update_occupant(self):
        self.occupants += 1
        self.save()

class Profile(models.Model):
    name = models.CharField(max_length = 30)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length = 30)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length = 60)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    description = models.TextField(null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    
    def find_business(cls,business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self):
        self.save()

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    user = models.ForeignKey (User, on_delete = models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment =  models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    