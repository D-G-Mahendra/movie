from rest_framework import serializers

from .models import User
from .models import MovieRatingDetail
from .models import Token

from movielist_app.models import Genre
from movielist_app.models import Movie

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fname = serializers.CharField(max_length=250)
    lname = serializers.CharField(max_length=250)
    mobile = serializers.CharField(max_length=100,required = False)
    email = serializers.EmailField(required = False)
    dob = serializers.DateField(required = False)
    age = serializers.IntegerField(required = False)
    prefered_genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(),many=True,required=False)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)
    
    def create(self,validated_data):
        genre_preferred=validated_data.pop('prefered_genre',[])
        user= User.objects.create(**validated_data)
        user.prefered_genre.set(genre_preferred)
        return user

    
    def update(self,instance, validated_data):
        genre_ids = validated_data.pop('prefered_genre',[])
        for k,v in validated_data.items():
            setattr(instance,k,v)
        instance.save()
        instance.prefered_genre.set(genre_ids)
        return instance

class MovieRatingSerializer(serializers.Serializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=MovieRatingDetail.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    comment = serializers.CharField(max_length=250)
    rating = serializers.IntegerField(required=False)
    like = serializers.BooleanField(required=False)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        movierating =MovieRatingDetail.object.create(**validated_data)
        return movierating

    def update(self,instance,validated_data):
        for k,v in validated_data.items():
            setattr(instance,k,v)
            instance.save()
        return instance

class TokenSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    token = serializers.CharField(max_length=255)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        movierating =MovieRatingDetail.object.create(**validated_data)
        return movierating

    def update(self,instance,validated_data):
        for k,v in validated_data.items():
            setattr(instance,k,v)
            instance.save()
        return instance
