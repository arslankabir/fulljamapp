# Generated by Django 2.2.4 on 2019-10-29 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0017_auto_20191028_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomment',
            name='post_owner',
        ),
    ]
