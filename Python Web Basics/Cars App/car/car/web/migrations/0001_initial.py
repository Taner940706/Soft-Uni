# Generated by Django 4.1.2 on 2022-10-30 08:38

import car.web.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10, verbose_name='Type')),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Model')),
                ('year', models.IntegerField(validators=[car.web.validators.validate_between_years], verbose_name='Year')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)], verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[car.web.validators.validate_min_len_username], verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)], verbose_name='Age')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]
