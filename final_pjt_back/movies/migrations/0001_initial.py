# Generated by Django 3.2.13 on 2022-11-23 21:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('trim_title', models.CharField(max_length=100)),
                ('trim_original_title', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('vote_count', models.IntegerField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('video_url', models.CharField(blank=True, max_length=200, null=True)),
                ('actors', models.ManyToManyField(to='movies.Actor')),
                ('directors', models.ManyToManyField(to='movies.Director')),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('like_movie_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('providers', models.ManyToManyField(to='movies.Provider')),
            ],
        ),
    ]
