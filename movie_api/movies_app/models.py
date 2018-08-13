from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()


class Comment(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )


