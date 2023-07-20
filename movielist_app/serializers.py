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


    # def update(self, instance,validated_data):
    #     genre_id = validated_data.pop("genre", [])
    #     for k,v in validated_data.items():
    #         setattr(instance,k,v)
    #     instance.save()
    #     instance.genre.set(genre_id)
    #     return instance

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.average_rating = validated_data.get('average_rating', instance.average_rating)
        instance.total_like = validated_data.get('total_like', instance.total_like)
        instance.total_review = validated_data.get('total_review', instance.total_review)
        instance.released_date = validated_data.get('released_date', instance.released_date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.director = validated_data.get('director', instance.director)

        if genre_data:
            instance.genre.set(genre_data)

        instance.save()

        return instance


class DirectorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Director.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     for k, v in validated_data.items():
    #         setattr(instance, k, v)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.created_on = validated_data.get('created_on', instance.created_on)
        instance.updated_on = validated_data.get('updated_on', instance.updated_on)

        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    genre = serializers.CharField(max_length=100)

    def create(self, validated_data):
        genre = Genre.objects.create(**validated_data)
        return genre
    # def update(self,instance,validated_data):
    #     for k,v in validated_data.items():
    #         setattr(instance, k, v)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.genre =validated_data.get('genre', instance.genre)

        instance.save()
        return instance