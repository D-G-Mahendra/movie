from rest_framework import serializers

from movielist_app.serializers import GenreSerializer, MovieSerializer
from .models import User
from .models import MovieRatingDetail
from .models import Token

from movielist_app.models import Genre
from movielist_app.models import Movie

def fname_with(value):
    if value[1].lower == 'ss':
        raise serializers.ValidationError('fname should not start with SS')
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fname = serializers.CharField(max_length=250, validators=[fname_with])
    lname = serializers.CharField(max_length=250)
    mobile = serializers.CharField(max_length=100,required = False)
    email = serializers.EmailField(required = False)
    dob = serializers.DateField(required = False)
    age = serializers.IntegerField(required = False)
    prefered_genre = GenreSerializer(many=True, required=False)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data, user_data=None):

        fname = validated_data.get('fname')
        lname = validated_data.get('lname')
        mobile = validated_data.get('mobile')
        email = validated_data.get('email')
        dob = validated_data.get('dob')
        age = validated_data.get('age')
        user = User.objects.create(
            fname=fname,
            lname=lname,
            mobile=mobile,
            email=email,
            dob=dob,
            age=age,
        )
        prefered_genre_id = self.initial_data.get('prefered_genre',[])
        if prefered_genre_id:
            prefered_genres = Genre.objects.filter(pk__in=[prefered_genre['id'] for prefered_genre in prefered_genre_id])
            user.prefered_genre.set(prefered_genres)
        return user

    def update(self, instance, validated_data):
        prefered_genre_id = validated_data.get('prefered_genre', [])

        instance.id = validated_data.get('id', instance.id)
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.age = validated_data.get('age', instance.age)

        if prefered_genre_id:
            prefered_genre =[prefered_genre['id'] for prefered_genre in prefered_genre_id]
            prefered_genres = Genre.objects.filter(
                pk__in=prefered_genre)
            instance.prefered_genre.set(prefered_genres)

        instance.save()
        return instance
    def validate_age(self, value):
        if value < 20:
            raise serializers.ValidationError('age should be greater than 20')
        return value

    def validate(self, data):
        fn = data.get('fname')
        ln = data.get('lname')
        if fn == ln:
            raise serializers.ValidationError(' fname and lname should not be same')
        return data

def user_name(value):
    if value[2].lower() != 'ss':
        raise serializers.ValidationError('SS not the user')
class MovieRatingDetailSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True, validators=[user_name])
    comment = serializers.CharField(max_length=250)
    rating = serializers.IntegerField(required=False)
    like = serializers.BooleanField(required=False)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        user = User.objects.get(pk=self.initial_data.get('user')["id"]) # getting the instance of user
        movie = Movie.objects.get(pk=self.initial_data.get('movie')["id"]) # getting the instance of movie
        comment = validated_data.get('comment')
        rating = validated_data.get('rating')
        like = validated_data.get('like')

        movieratingdetail = MovieRatingDetail.objects.create(
            user= user,
            movie=movie,
            comment =comment,
            rating = rating,
            like= like
        )
        return movieratingdetail

    def update(self, instance, validated_data):
        # instance.user = validated_data.get('user', instance.user)
        # instance.movie = validated_data.get('movie', instance.movie)

        user_data = self.initial_data.get('user', None).get('id', None)
        instance.user = User.objects.get(pk=user_data)
        movie_data = self.initial_data.get('movie', None).get('id', None)
        instance.movie = Movie.objects.get(pk=movie_data)
        instance.id = validated_data.get('id', instance.id)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.like = validated_data.get('like', instance.like)

        instance.save()
        return instance
    def validate_rating(self,value):
        if value < 2:
            raise serializers.ValidationError('Movie is not good')
        return value
    def validate(self, data):
        r =data.get('rating')
        l =data.get('like')
        if r==l:
            raise serializers.ValidationError('rating and like should not be same')
        return data

def token_name(value):
    if value[0] == '3':
        raise serializers.ValidationError('Aditya should not be fname')
class TokenSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    token = serializers.CharField(max_length=255, validators=[token_name])
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        user = User.objects.get(pk=self.initial_data.get('user')["id"])
        token = validated_data.get('token')
        token = Token.objects.create(
            user=user,
            token=token
        )
        return token

    def update(self, instance, validated_data):
        #instance.user = validated_data.get('user', instance.user)
        user_data = self.initial_data.get('user', None).get('id', None)
        instance.user = User.objects.get(pk=user_data)
        instance.token = validated_data.get('token', instance.token)

        instance.save()
        return instance

    def validate_token(self, value):
        if value ==3:
            raise serializers.ValidationError('if token is 3 user should aditya')
        return value

    def validate(self, data):
        us = data.get('user')
        to = data.get('token')
        if to ==3 and us == 'Aditya':
            raise serializers.ValidationError('aditya should not be user')