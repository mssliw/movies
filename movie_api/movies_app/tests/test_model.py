from django.test import TestCase
from ..models import Movie, Rating, Comment


class MovieModelTest(TestCase):

    def create_movie(self, title='Test movie'):
        return Movie.objects.create(title=title)

    def test_create_movie(self):
        movie = self.create_movie()
        self.assertTrue(isinstance(movie, Movie))
        self.assertEqual(movie.__str__(), movie.title)


class CommentModelTest(TestCase):
    def create_comment(self, comment='Testing comment'):
        movie = Movie.objects.create(title='Test movie')
        return Comment.objects.create(comment=comment, movie=movie)

    def test_create_comment(self):
        comment = self.create_comment()
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.__str__(), comment.comment)


class RatingModelTest(TestCase):
    def create_rating(self, source='Test source'):
        movie = Movie.objects.create(title='Test movie')
        return Rating.objects.create(source=source, movie=movie)

    def test_create_rating(self):
        rating = self.create_rating()
        self.assertTrue(isinstance(rating, Rating))
        self.assertEqual(rating.__str__(), rating.source)
