import pdb

from django.shortcuts import render
from rest_framework import status

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from movielist_app.models import Movie, Director, Genre
from movielist_app.serializers import MovieSerializer, DirectorSerializer, GenreSerializer


class MovieList(APIView):
    def get(self,request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class MovieDetails(APIView):
    def get(self,request,pk):
        queryset = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk,):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk,):
        movie = Movie.objects.get(pk=pk)
        movie = movie.delete()
        return Response(movie)

class DirectorView(APIView):
    def get(self,request):
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class DirectorDetails(APIView):
    def get(self,request,pk):
        queryset = Director.objects.get(pk=pk)
        serializer = DirectorSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk,):
        director = Director.objects.get(pk=pk)
        serializer = DirectorSerializer(director, data=request.data)# if we will pass instance objects to the serializer it call update method insude the serializet
        #else it will create new oblect.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk,):
        director = Director.objects.get(pk=pk)
        director = director.delete()
        return Response(director)

class GenreView(APIView):

    def get(self,request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GenreDetailsView(APIView):
    def get(self,request, pk):
        genre=Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self,request, pk):
        genre = Genre.objects.get(pk=pk)
        #import pdb;pdb.set_trace()
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()  # this will call create/update method from serializer
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request, pk):
        genre = Genre.objects.get(pk=pk)
        genre = genre.delete()
        return Response(genre)