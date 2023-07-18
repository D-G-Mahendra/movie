from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from movielist_app.models import Movie
from movielist_app.serializers import MovieSerializer
from user.models import User, MovieRatingDetail, Token
from user.serializers import UserSerializer, MovieRatingSerializer, TokenSerializer


# Create your views here.
class UserView(APIView):
    def get(self,request):
        queryset=User.objects.all()
        serializer= UserSerializer(queryset, many=True,)
        return Response(serializer.data)

    def post(self,request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

class UserDetails(APIView):

    def get(self,request,pk):
        queryset=User.objects.get(pk=pk)
        serializer= UserSerializer(queryset)
        return Response(serializer.data)
    def put(self,request,pk):
        queryset=User.objects.get(pk=pk)
        serializer=UserSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.error)

    def delete(self,request,pk):
        queryset=User.objects.get(pk=pk)
        user= queryset.delete()
        return Response(user)

class MovieRatingView(APIView):
    def get(self,request):
        queryset=MovieRatingDetail.objects.all()
        serializer= MovieRatingSerializer(queryset, many=True,)
        return Response(serializer.data)

    def post(self,request):
        serializer= MovieRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

class MovieRatingDetailsView(APIView):

    def get(self,request,pk):
        queryset=MovieRatingDetail.objects.get(pk=pk)
        serializer= MovieRatingSerializer(queryset)
        return Response(serializer.data)
    def put(self,request,pk):
        queryset=MovieRatingDetail.objects.get(pk=pk)
        serializer=MovieRatingSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.error)

    def delete(self,request,pk):
        queryset=MovieRatingDetail.objects.get(pk=pk)
        rating= queryset.delete()
        return Response(rating)

class TokenView(APIView):
    def get(self,request):
        queryset=Token.objects.all()
        serializer= TokenSerializer(queryset, many=True,)
        return Response(serializer.data)

    def post(self,request):
        serializer= TokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

class TokenDetailsView(APIView):

    def get(self, request, pk):
        queryset=Token.objects.get(pk=pk)
        serializer= TokenSerializer(queryset)
        return Response(serializer.data)
    def put(self, request, pk):
        queryset=Token.objects.get(pk=pk)
        serializer=TokenSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.error)

    def delete(self, request, pk):
        queryset=Token.objects.get(pk=pk)
        rating= queryset.delete()
        return Response(rating)

