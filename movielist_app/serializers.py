from rest_framework import serializers

from movielist_app.models import Director, Genre, Movie


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    description = serializers.CharField(required=False)
    average_rating = serializers.IntegerField(required=False)
    total_like = serializers.IntegerField(required=False)
    total_review = serializers.IntegerField(required=False)
    released_date = serializers.DateField(required=False)
    duration = serializers.CharField(max_length=100, required=False)
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())
    genre = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    def create(self, validated_data):
        genre_id = validated_data.pop('genre', [])
        movie = Movie.objects.create(**validated_data)
        movie.genre.set(genre_id)
        return movie
