from rest_framework import serializers
from .models import Movie, Rating, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'source',
            'value',
        )


class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id',
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
            'imdbrating',
            'imdbid',
            'type',
            'boxoffice',
            'production',
            'website',
            'ratings',
            'comments'
        )
