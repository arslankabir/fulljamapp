# Generated by Django 2.2.4 on 2019-10-18 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('datetimepicker', models.CharField(blank=True, max_length=10, null=True)),
                ('p_photo', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('h_photo', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('subtitles', models.CharField(blank=True, max_length=20, null=True)),
                ('about_me', models.TextField(blank=True, max_length=200, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=20, null=True)),
                ('lives_in', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('province', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('occupation', models.CharField(blank=True, max_length=20, null=True)),
                ('relationship_status', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('religious_belifs', models.CharField(blank=True, max_length=20, null=True)),
                ('political_incline', models.CharField(blank=True, max_length=20, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('RSS', models.CharField(blank=True, max_length=255, null=True)),
                ('dibble', models.CharField(blank=True, max_length=255, null=True)),
                ('spotify', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HobbiesAndInterests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('fav_music', models.TextField(blank=True, null=True)),
                ('fav_tv_shows', models.TextField(blank=True, null=True)),
                ('fav_books', models.TextField(blank=True, null=True)),
                ('fav_movies', models.TextField(blank=True, null=True)),
                ('fav_writers', models.TextField(blank=True, null=True)),
                ('fav_games', models.TextField(blank=True, null=True)),
                ('other_interests', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile_place1', models.TextField(blank=True, null=True)),
                ('period1', models.TextField(blank=True, null=True)),
                ('description1', models.TextField(blank=True, null=True)),
                ('titile_place2', models.TextField(blank=True, null=True)),
                ('period2', models.TextField(blank=True, null=True)),
                ('description2', models.TextField(blank=True, null=True)),
                ('titile_place3', models.TextField(blank=True, null=True)),
                ('period3', models.TextField(blank=True, null=True)),
                ('description3', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
