import requests

from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, View
from django.views.generic.edit import FormView

from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import SubmitMovieForm
from .models import Movie, Comment, Rating
from .serializers import (
    MovieSerializer,
    RatingSerializer,
    CommentSerializer
)


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
    renderer_classes = TemplateHTMLRenderer
    template_name = 'movies.html'
    form_class = SubmitMovieForm
    success_url = 'tldr/'
    search_result = {}

    # def get_queryset(self):
    #     queryset = Movie.objects.all()
    #     # Set up eager loading to avoid N+1 selects
    #     queryset = self.get_serializer_class().setup_eager_loading(queryset)
    #     return queryset

    def form_valid(self, form):
        title = form['title'].data
        print('requested title: ', form['title'].data)
        if Movie.objects.filter(title__iexact=title).exists():
            movie = Movie.objects.filter(title__iexact=title).first()
            serializer = MovieSerializer(movie)
            print(title, ' already exists')
            return JsonResponse(serializer.data)
        else:
            search_result = form.search()
            data = dict((key.lower(), value) for key, value in search_result.items())
            serializer = MovieSerializer(data=data)

            if search_result['success']:
                response_status = search_result['Response']

                if response_status and serializer.is_valid():
                    print('response is ', response_status, ' serializer is valid')
                    movie = serializer.save()
                    movie_id = movie.id
                    print('movie id ', movie_id)
                    ratings = search_result['Ratings']
                    print('ratings ', ratings, type(ratings))

                    for rating in ratings:
                        rating_data = dict((key.lower(), value) for key, value in rating.items())
                        # rating_data.update({'movie': movie})
                        print(rating_data, ' rating', type(rating))
                        rating_serializer = RatingSerializer(data=rating_data)
                        if rating_serializer.is_valid():
                            print(rating_serializer)
                            rating_source = str(rating_serializer['source'].value)
                            rating_value = str(rating_serializer['value'].value)
                            print(rating_source, rating_value)
                            rating = Rating(movie=movie, source=rating_source, value=rating_value)
                            print(rating)
                            rating.save()
                        else:
                            print(rating_serializer.errors)

                            print('sth wrong')
                    return JsonResponse(serializer.data)
                    print(movie.ratings)
                else:
                    print('serializer not valid or status wrong')
                    print(response_status, serializer.is_valid())
                    print(serializer.errors)
            else:
                pass
        # return super().form_valid(form)
            return JsonResponse(search_result)
