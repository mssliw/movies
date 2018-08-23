import requests

from django.conf import settings
from django.http import Http404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie, Comment, Rating
from .serializers import (
    MovieSerializer,
    RatingSerializer,
    CommentSerializer
)


class MoviesListView(APIView):
    """
    List of movies existing in database
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # filter_backends = (DjangoFilterBackend)
    # filter_fields = ('title', 'id')

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

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

        serializer = MovieSerializer(data=request.data)
        title = request.data.get('title')

        if serializer.is_valid():
            search_result = search(title)
            fetched_data = dict((key.lower(), value)
                                for key, value in search_result.items())
            serializer = MovieSerializer(data=fetched_data)

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
                            rating_source = str(
                                rating_serializer['source'].value)
                            rating_value = str(
                                rating_serializer['value'].value)
                            rating = Rating(movie=movie,
                                            source=rating_source,
                                            value=rating_value)
                            rating.save()
                        else:
                            print(rating_serializer.errors)
                    return Response(serializer.data)
                else:
                    print(response_status,
                          serializer.is_valid(),
                          serializer.errors)
            else:
                print('search result is wrong')

            return Response(title, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class MovieDetailsView(APIView):
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


class CommentView(APIView):
    """
    List of comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, pk, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_body = str(
                comment_serializer['comment'].value)
            movie = int(
                comment_serializer['movie'].value)
            commented_movie = Movie.objects.get(id=movie)
            comment = Comment(comment=comment_body, movie=commented_movie)
            comment.save()
            return Response(comment_serializer.data)


class MovieCommentsView(APIView):
    """
    Title-based movie details
    """

    def get_object(self, pk):
        try:
            return Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data['comments'])
