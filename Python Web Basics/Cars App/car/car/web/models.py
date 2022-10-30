from django.core import validators
from django.db import models
from car.web.validators import validate_min_len_username, validate_between_years


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    AGE_MIN_VALUE = 18
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_LEN = 30
    LAST_NAME_LEN = 30
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(validate_min_len_username,),
        null=False,
        blank=False,
        verbose_name="Username",
    )
    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name='Email',
    )

    age = models.IntegerField(
        validators=(validators.MinValueValidator(AGE_MIN_VALUE),),
        null=False,
        blank=False,
        verbose_name='Age',
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='Password',
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_LEN,
        null=True,
        blank=True,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=LAST_NAME_LEN,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )


class Car(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CARS = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )
    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=CARS,
        null=False,
        blank=False,
        verbose_name='Type'
    )
    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=(validators.MinLengthValidator(MODEL_MIN_LEN),),
        null=False,
        blank=False,
        verbose_name='Model'
    )
    year = models.IntegerField(
        validators=(validate_between_years,),
        null=False,
        blank=False,
        verbose_name='Year',
    )
    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        validators=(validators.MinValueValidator(1.0),),
        blank=False,
        null=False,
        verbose_name='Price',

    )

