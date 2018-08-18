# Generated by Django 2.1 on 2018-08-18 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0007_auto_20180818_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbrating',
            field=models.CharField(max_length=10),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies_app.Movie'),
            preserve_default=False,
        ),
    ]
