# Generated by Django 2.2.4 on 2019-10-26 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0015_auto_20191026_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='cr_date',
            new_name='cm_cr_date',
        ),
        migrations.RenameField(
            model_name='usercomment',
            old_name='likes',
            new_name='cm_likes',
        ),
    ]
