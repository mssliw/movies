from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Movie, Comment
from .serializes import MovieSerializer, CommentSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# def index(request):
#     return HttpResponse("Hello, world, you're at the movies app index")

