from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
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
    source = models.CharField(max_length=200)
    value = models.CharField(max_length=10)
    movie = models.ForeignKey(
        Movie,
        related_name='ratings',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.source

    def save(self, *a, **kw):
        for field in self._meta.fields:
            if isinstance(field, Rating):
                id_attname = field.attname
                instance_attname = id_attname.rpartition("_id")[0]
                instance = getattr(self, instance_attname)
                instance_id = instance.pk
                setattr(self, id_attname, instance_id)

        return Rating.save(self, *a, **kw)


class Comment(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment
