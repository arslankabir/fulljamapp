# Generated by Django 2.2.4 on 2019-10-24 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191023_1536'),
        ('olympus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_cr_date', models.DateTimeField(auto_now_add=True)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
                ('liked_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympus.UserPost')),
            ],
        ),
    ]
