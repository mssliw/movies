from django.db import models


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=20, blank=True)
    rate = models.CharField(max_length=10, blank=True)
    release = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
    )
    runtime = models.CharField(max_length=10, blank=True)
    genre = models.TextField(blank=True)
    director = models.CharField(max_length=200, blank=True)
    writer = models.TextField(blank=True)
    plot = models.TextField(blank=True)
    language = models.CharField(max_length=50,blank=True)
    country = models.CharField(max_length=100, blank=True)
    awards = models.TextField(blank=True)
    poster = models.TextField(blank=True)
    metascore = models.IntegerField(blank=True, null=True)
    imdbrating = models.CharField(max_length=10, blank=True)
    imdbid = models.TextField(blank=True)
    type = models.TextField(blank=True)
    dvd = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
    )
    boxoffice = models.TextField(blank=True)
    production = models.TextField(blank=True)
    website = models.TextField(blank=True)
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
