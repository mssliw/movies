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
from rest_framework.views import APIView
from .forms import SubmitMovieForm
from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer


class MoviesList(APIView):
    '''
    List all of the movies or create a new movie record
    '''
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetails(APIView):
    '''
    Retrieve, update or delete a movie
    '''
    def get_object(self, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
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


