# Generated by Django 2.1 on 2018-08-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0003_auto_20180823_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbrating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
