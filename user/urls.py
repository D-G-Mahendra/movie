from django.urls import path
from django.conf.urls import include

from .views import UserAPIView,UserDetailAPIView,MovieRatingDetailAPIView,MovieRatingDetailsAPIView,TokenAPIView
urlpatterns = [
    path('',UserAPIView.as_view(),name="user_api"),
    path('<int:pk>/',UserDetailAPIView.as_view(),name="user_detail_api"),
    path('mrd/',MovieRatingDetailAPIView.as_view(),name="mrd_api"),
    path('mrd/<int:pk>',MovieRatingDetailsAPIView.as_view(),name="mrd_detail_api"),
    path('token/',TokenAPIView.as_view(),name= "token_api"),
]