from django.urls import path
from watchListApp.api.views import movie_details, movie_list

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    path('list/<int:pk>', movie_details, name='movie-detail'),
]