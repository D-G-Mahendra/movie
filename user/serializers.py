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
    
    # def create(self,validated_data):
    #     genre_preferred=validated_data.pop('prefered_genre',[])
    #     user= User.objects.create(**validated_data)
    #     user.prefered_genre.set(genre_preferred)
    #     return user

    def create(self, instance, validated_data):
        prefered_genre_id = validated_data.pop('prefered_genre', [])
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.age = validated_data.get('age', instance.age)
        if prefered_genre_id:
            instance.prefered_genre.set(prefered_genre_id)
        instance.save()
        return instance
    
    # def update(self,instance, validated_data):
    #     genre_ids = validated_data.pop('prefered_genre',[])
    #     for k,v in validated_data.items():
    #         setattr(instance,k,v)
    #     instance.save()
    #     instance.prefered_genre.set(genre_ids)
    #     return instance


    def update(self, instance, validated_data):
        prefered_genre_id = validated_data.pop('prefered_genre', [])

        instance.id = validated_data.get('id', instance.id)
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.age = validated_data.get('age', instance.age)

        if prefered_genre_id:
            instance.prefered_genre.set(prefered_genre_id)
        instance.save()
        return instance

class MovieRatingDetailSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    movie = serializers.PrimaryKeyRelatedField(queryset = Movie.objects.all())

    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    comment = serializers.CharField(max_length=250)
    rating = serializers.IntegerField(required=False)
    like = serializers.BooleanField(required=False)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    # def create(self,validated_data):
    #     movierating =MovieRatingDetail.object.create(**validated_data)
    #     return movierating
    #
    def create(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.like = validated_data.get('like', instance.like)
        instance.save()
        return instance
    
    # def update(self,instance,validated_data):
    #     for k,v in validated_data.items():
    #         setattr(instance,k,v)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.id = validated_data.get('id', instance.id)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.like = validated_data.get('like', instance.like)

        instance.save()
        return instance

class TokenSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    token = serializers.CharField(max_length=255)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    # def create(self,validated_data):
    #     movierating =MovieRatingDetail.object.create(**validated_data)
    #     return movierating

    def create(self,instance,validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.token = validated_data.get('token', instance.token)
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     user_id = validated_data.pop('user', [])
    #
    #     for k,v in validated_data.items():
    #         setattr(instance,k,v)
    #
    #     instance.save()
    #     instance.user.set(user_id)
    #     return instance

    def update(self,instance,validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.token = validated_data.get('token', instance.token)

        instance.save()
        return instance
