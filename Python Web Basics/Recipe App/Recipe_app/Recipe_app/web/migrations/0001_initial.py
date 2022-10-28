# Generated by Django 4.1.2 on 2022-10-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_url', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('ingredients', models.CharField(max_length=250)),
                ('time', models.IntegerField()),
            ],
        ),
    ]
