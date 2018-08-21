from django.db import models


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    rate = models.CharField(max_length=10, default='')
    release = models.DateField(
        auto_now=False,
        auto_now_add=False,
        default='2000-01-01'
    )
    runtime = models.CharField(max_length=10)
    genre = models.TextField(default='')
    director = models.CharField(max_length=200, default='')
    writer = models.TextField(default='')
    plot = models.TextField(default='')
    language = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=100, default='')
    awards = models.TextField(default='')
    poster = models.TextField(default='')
    metascore = models.IntegerField(default=0)
    imdbrating = models.CharField(max_length=10)
    imdbid = models.TextField(default='')
    type = models.TextField(default='')
    dvd = models.DateField(default='2000-01-01')
    boxoffice = models.TextField(default='')
    production = models.TextField(default='')
    website = models.TextField(default='')
    response = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=200)
    value = models.CharField(max_length=10)
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    def __str__(self):
        return self.source


class Comment(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment
