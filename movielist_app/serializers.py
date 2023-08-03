from rest_framework import serializers

from movielist_app.models import Director, Genre, Movie

# def genre_name(value):
#     if value[0] == 3:
#         raise serializers.ValidationError('id should be Adventure')
class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    genre = serializers.CharField(max_length=100)

    def create(self, validated_data):
        genre =validated_data.get('genre')
        genre = Genre.objects.create(
            genre=genre
        )
        return genre # returning queryset

    def update(self, instance, validated_data):
        #instance.id = validated_data.get('id', instance.id)
        instance.genre =validated_data.get('genre', instance.genre)
        instance.save()
        return instance

    def validate_genre(self, value):
        if value =='Action':
            raise serializers.ValidationError('genre should change')
        return value

def name_start(value):
    if value[1].lower() != 'SS':
        raise serializers.ValidationError('SS is not Director')

class DirectorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_start])
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        name = validated_data.get('name')
        director = Director.objects.create(
            name=name
        )
        return director

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def validate_name(self, value):
        if value == 'Aditya':
            raise serializers.ValidationError(' dont write Author Name')
        return value

    def validate(self, data):
        nm = data.get('name')
        cd = data.get('created_on')
        if cd != ''and nm !='RRR' :
            raise serializers.ValidationError('updated date and created should not be same')
        return data
def title_with_a(value):
    if value[0].lower != 'aditya':
        raise serializers.ValidationError('name shoulld not start with Aditya')
class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500, validators=[title_with_a])
    description = serializers.CharField(required=False)
    average_rating = serializers.IntegerField(required=False)
    total_like = serializers.IntegerField(required=False)
    total_review = serializers.IntegerField(required=False)
    released_date = serializers.DateField(required=False)
    duration = serializers.CharField(max_length=100, required=False)
    director = DirectorSerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    def create(self,validated_data):

        title = validated_data.get('title')
        description = validated_data.get('description')
        average_rating = validated_data.get('average_rating')
        total_like = validated_data.get('total_like')
        total_review = validated_data.get('total_review')
        released_date = validated_data.get('released_date')
        duration = validated_data.get('duration')
        director = Director.objects.get(pk= self.initial_data.get('director')['id'])
        movie = Movie.objects.create(

            title =title,
            description=description,
            average_rating=average_rating,
            total_like=total_like,
            total_review=total_review,
            released_date=released_date,
            duration=duration,
            director=director
        )

        genre_data = self.initial_data.get('genre')
        if genre_data:
            genres = Genre.objects.filter(pk__in=[genre['id'] for genre in genre_data])
            movie.genre.set(genres)
        return movie

    def update(self, instance, validated_data):
        #genre_data = validated_data.pop('genre', [])

        #director = Director.objects.get(pk=2) calling object using id
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.average_rating = validated_data.get('average_rating', instance.average_rating)
        instance.total_like = validated_data.get('total_like', instance.total_like)
        instance.total_review = validated_data.get('total_review', instance.total_review)
        instance.released_date = validated_data.get('released_date', instance.released_date)
        instance.duration = validated_data.get('duration', instance.duration)
        #instance.director = validated_data.get('director', instance.director)
        #instance.director = director updating the object instance

        director_data = self.initial_data.get('director', None).get('id', None)
        instance.director =Director.objects.get(pk=director_data)

        genre_data = self.initial_data.get('genre', [])
        if genre_data:
            genres = Genre.objects.filter(pk__in=[genre['id'] for genre in genre_data])
            instance.genre.set(genres)

        # genre_data = self.initial_data['genre']
        # genreinstance = []
        # for genre in genre_data:
        #     genreinstance.append(Genre.objects.get(pk=genre['id']))
        # instance.genre.set(genreinstance)

        instance.save()
        return instance
    def validate_average_rating(self, value):
        if value > 5:
            raise serializers.ValidationError('rating should not be greater than 5')
        return value

    def validate(self, data):
        ar =data.get('average_rating')
        li = data.get('total_like')
        if ar > 3 and li != 2:
            raise  serializers.ValidationError('ar and li is compared, likes must be 2')
        return data






