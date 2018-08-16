from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment



