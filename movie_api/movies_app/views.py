import requests

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .forms import SubmitMovieForm
from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer

@api_view(['GET', 'POST'])
def movies_list(request, format=None):
    '''
    List all of the movies or create a new movie record
    '''
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk, format=None):
    '''
    Retrieve, update or delete a movie
    '''
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class MovieView(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class RequestView(TemplateView):
#     # template_name = 'movies.html'
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#     @action(methods=['post'], detail=True)
#     def save_movie(self, request):
#         form = SubmitMovieForm(request.POST)
#         if form.is_valid():
#             url = form.cleaned_data['url']
#             print(url)
#             r = request.get('http://www.omdbapi.com/?apikey=' + settings.OMDB_KEY + '&t=' + url)
#             json = r.json()
#             print(json)
#             serializer = MovieSerializer(data=json)
#             if serializer.is_valid():
#                 movie = serializer.save()
#                 return HttpResponseRedirect('')
#             else:
#                 form = SubmitMovieForm()
#         return render(request, 'movies.html', {'form': SubmitMovieForm()}, movies=queryset)


