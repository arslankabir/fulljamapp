# Generated by Django 2.2.4 on 2019-10-26 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0007_usercomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='date',
            new_name='cr_date',
        ),
    ]
