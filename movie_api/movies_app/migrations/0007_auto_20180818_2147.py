# Generated by Django 2.1 on 2018-08-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_auto_20180818_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ManyToManyField(to='movies_app.Movie'),
        ),
    ]
