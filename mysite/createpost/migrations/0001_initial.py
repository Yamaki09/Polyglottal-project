# Generated by Django 4.2.dev20221206114816 on 2022-12-10 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
    ]
