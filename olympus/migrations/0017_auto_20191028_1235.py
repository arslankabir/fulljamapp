# Generated by Django 2.2.4 on 2019-10-28 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0016_auto_20191026_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='comment_post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='usercomment',
            old_name='posted_by',
            new_name='post_owner',
        ),
    ]
