# Generated by Django 2.2.4 on 2019-10-26 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olympus', '0009_auto_20191026_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='olympus.UserPost'),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
    ]
