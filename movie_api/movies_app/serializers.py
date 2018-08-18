from rest_framework import serializers
from .models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'title',
            'year',
            'rate',
            'release',
            'runtime',
            'genre',
            'director',
            'writer',
            'plot',
            'language',
            'country',
            'awards',
            'poster',
            'metascore',
            'imdbrating',
            'imdbid',
            'type',
            'boxoffice',
            'production',
            'website',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'comment'
