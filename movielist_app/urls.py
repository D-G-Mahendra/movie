from django.urls import path
from .views import MovieList, MovieDetails, DirectorView, DirectorDetails, GenreView, GenreDetailsView

urlpatterns = [
    path('movie/', MovieList.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetails.as_view(), name='moviedetails'),
    path('director/', DirectorView.as_view(), name='movie_list'),
    path('director/<int:pk>/', DirectorDetails.as_view(),name='directordetails'),
    path('genre/', GenreView.as_view(),name='genre'),
    path('genre/<int:pk>/', GenreDetailsView.as_view(), name='genredetails')
]
