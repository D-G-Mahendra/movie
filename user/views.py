from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from movielist_app.models import Movie
from movielist_app.serializers import MovieSerializer


# Create your views here.

