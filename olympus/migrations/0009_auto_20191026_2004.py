# Generated by Django 2.2.4 on 2019-10-26 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0008_auto_20191026_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='image',
            new_name='c_image',
        ),
        migrations.RenameField(
            model_name='usercomment',
            old_name='text',
            new_name='comment',
        ),
    ]
