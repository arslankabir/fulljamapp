# Generated by Django 2.2.4 on 2019-11-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0022_userpost_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to='accounts.UserProfile'),
        ),
    ]
