from django.core import validators
from django.db import models


class Profile(models.Model):
    AGE_MIN_LEN = 12
    PASS_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name='Email',
    )
    age = models.IntegerField(
        validators=(validators.MinValueValidator(AGE_MIN_LEN),),
        null=False,
        blank=False,
        verbose_name="Age",
    )
    password = models.CharField(
        max_length=PASS_MAX_LEN,
        null=False,
        blank=False,
        verbose_name="Password"
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=False,
        verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=False,
        verbose_name="Last Name"
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    RATING_MAX_LEN = 5.0
    RATING_MIN_LEN = 1.0
    MAX_LEVEL_MIN_LEN = 1
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = 'Puzzle'
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = 'Other'

    GAMES = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Title",
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=GAMES,
        null=False,
        blank=False,
        verbose_name='Category'

    )
    rating = models.FloatField(
        max_length=RATING_MAX_LEN,
        validators=(validators.MinValueValidator(RATING_MIN_LEN), ),
        null=False,
        blank=False,
        verbose_name="Rating",
    )
    max_level = models.IntegerField(
        validators=(validators.MinValueValidator(MAX_LEVEL_MIN_LEN),),
        null=True,
        blank=True,
        verbose_name="Max Level",
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )
    summary = models.TextField(
        null=True,
        blank=True,
        verbose_name='Summary',
    )