from django.shortcuts import render
from rest_framework import status

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from movielist_app.models import Movie
from movielist_app.serializers import MovieSerializer


class MovieList(APIView):
    def get(self,request,pk):
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
        movie = Movie.objects.get(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk,):
        movie = Movie.objects.get(pk)
        movie.delete()
        return Response(movie)
