from django.urls import path
from django.conf.urls import include
from .views import UserView, UserDetails, MovieRatingView, MovieRatingDetailsView, TokenView, TokenDetailsView

urlpatterns = [

    path('user/', UserView.as_view(), name='userView'),
    path('user/<int:pk>/', UserDetails.as_view(), name='detailsView'),
    path('movierating/', MovieRatingView.as_view(), name='movieratingView'),
    path('movierating/<int:pk>/', MovieRatingDetailsView.as_view(), name='movieratingdetailsView'),
    path('token/', TokenView.as_view(), name='tokenView'),
    path('token/<int:pk>/', TokenDetailsView.as_view(), name='tokendetailsView'),
]