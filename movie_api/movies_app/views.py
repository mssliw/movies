import requests

from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.views.generic.edit import FormView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import SubmitMovieForm
from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer


class MoviesList(APIView):
    """
    List all of the movies or create a new movie record
    """
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
    """
    Retrieve, update or delete a movie
    """
    def get_object(self, pk):
        try:
            return Movie.objects.get(title=pk)
        except Movie.MultipleObjectsReturned:   #TODO: HANDLE NON-UNIQUE TITLES IF NEEDED
            raise Http404
        except Movie.DoesNotExist:  #TODO: get from external API
            raise Http404

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


class RequestApi(FormView):     #TODO: Save response to the db
    """
    Wip external-API handler

    """
    template_name = 'movies.html'
    form_class = SubmitMovieForm
    success_url = 'tldr/'
    search_result = {}

    def form_valid(self, form):
        print(form.fields['title'])

        search_result = form.search()
        print(search_result, ' VIEW TITLE')
        # return super().form_valid(form)
        return JsonResponse(search_result)
