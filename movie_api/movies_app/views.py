import requests

from django.conf import settings
from django.http import Http404


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie, Comment, Rating
from .serializers import (
    MovieSerializer,
    RatingSerializer,
    CommentSerializer
)


class MoviesList(APIView):
    """
    List of movies existing in database
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        title = request.data.get('title')

        def search(title):
            result = {}
            api_key = settings.OMDB_KEY
            url = 'http://www.omdbapi.com/?apikey={}&t={}'\
                .format(api_key, title)
            response = requests.get(url)
            if response.status_code == 200:
                result = response.json()
                result['success'] = True
            else:
                result['success'] = False
                if response.status_code == 404:
                    print('404')
                else:
                    print('error occured', response.status_code)
            return result

        search_result = search(title)
        print(search_result)
        data = dict((key.lower(), value)
                    for key, value in search_result.items())
        serializer = MovieSerializer(data=data)

        if search_result['success']:
            response_status = search_result['Response']

            if response_status and serializer.is_valid():
                movie = serializer.save()
                ratings = search_result['Ratings']

                for rating in ratings:
                    rating_data = dict((key.lower(), value)
                                       for key, value in rating.items())
                    rating_serializer = RatingSerializer(data=rating_data)
                    if rating_serializer.is_valid():
                        rating_source = str(rating_serializer['source'].value)
                        rating_value = str(rating_serializer['value'].value)
                        rating = Rating(movie=movie,
                                        source=rating_source,
                                        value=rating_value)
                        rating.save()
                    else:
                        print(rating_serializer.errors)
                        print('sth wrong')
                return Response(serializer.data)
            else:
                print('serializer not valid or status wrong')
                print(response_status, serializer.is_valid())
                print(serializer.errors)
        else:
            print('search result is wrong')

        return Response(title, status=status.HTTP_201_CREATED)


class MovieDetails(APIView):
    """
    Title-based movie details
    """

    def get_object(self, pk):
        try:
            return Movie.objects.get(title=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pk = Movie.objects.filter(title__iexact=pk).first()
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
