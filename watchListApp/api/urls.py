from django.urls import path
from watchListApp.api.views import MovieListAV, MovieDetailAV
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('list/<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
]