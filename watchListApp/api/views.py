from watchListApp.models import Movie
from watchListApp.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)