from django.db import models
from user.models import User
# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=512,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.name

MOVIE_GENRES = [
    ("Action", "Action"),
    ("Adventure", "Adventure"),
    ("Animation", "Animation"),
    ("Comedy", "Comedy"),
    ("Crime", "Crime"),
    ("Drama", "Drama"),
    ("Fantasy", "Fantasy"),
    ("Horror", "Horror"),
    ("Mystery", "Mystery"),
    ("Romance", "Romance"),
    ("Science Fiction", "Science Fiction"),
    ("Thriller", "Thriller"),
    ("Western", "Western"),
    ("Biography", "Biography"),
    ("Documentary", "Documentary"),
    ("Family", "Family"),
    ("Historical", "Historical"),
    ("Musical", "Musical"),
    ("Noir", "Noir"),
    ("Sports", "Sports"),
    ("War", "War")
]
"""" 
Important Points while creating serializers
1. we creating serializer for model 
2. we will be only looking only that model for which we are creating serializer
3. will implement create/update method inside serializer when it is required. 
"""
class Genre(models.Model):
    
    genre = models.CharField(max_length=50, choices=MOVIE_GENRES)

    def __str__(self):
        return self.genre
class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    average_rating = models.IntegerField(blank=True, default=0)
    total_like = models.IntegerField(blank=True, default=0)
    total_review = models.IntegerField(blank=True, default=0)
    released_date = models.DateField(blank=True, null=True)
    duration = models.CharField(blank=True, null=True,max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.title
    

    


    
    