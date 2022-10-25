from django.db import models
from django.core import validators

class Profile(models.Model):
	MIN_LEN_AGE = 12
	MAX_LEN_FIRST_NAME = 30
	MAX_LEN_LAST_NAME = 30
	email = EmailField(
		null=False,
		blank=False,
		verbose_name = "Email"
		),
	age = IntegerField(
		null=False,
		blank=False,
		validators=(MinLengthValidator(MIN_LEN_AGE),),
		verbose_name = "Age"
		)
	first_name = CharField(
		null=True,
		blank=True,
		max_length=MAX_LEN_FIRST_NAME,
		verbose_name="First Name")
	last_name = CharField(
		null=True,
		blank=True,
		max_length=MAX_LEN_LAST_NAME,
		verbose_name="Last Name")
	profile_image = URLField(
		null=True,
		blank=True,
		verbose_name="Profile Picture")


class Game(models.Model):
	TITLE_MAX_LEN=30
	CATEGORY_MAX_LEN = 15
	RATING_MAX_LEN = 5.0
	RATING_MIN_LEN_AGE = 0.1
	MAX_LEVEL_LEN = 1

	ACTION = "Action"
	ADVENTURE = "Adventure"
	PUZZLE = "Puzzle"
	STRATEGY = "Strategy"
	SPORTS = "Sports"
	BOARD_CARD = "Board/Card Game"
	OTHER = "Other"

	GAMES = (
		(ACTION, ACTION),
		(ADVENTURE, ADVENTURE),
		(PUZZLE, PUZZLE),
		(STRATEGY, STRATEGY),
		(SPORTS, SPORTS),
		(BOARD_CARD, BOARD_CARD),
		(OTHER, OTHER),
		)

	title = models.CharField(
		blank=False,
		null=False,
		unique = True,
		max_length = TITLE_MAX_LEN,
		verbose_name = "Title")

	category = models.CharField(
		blank=False,
		null=False,
		choices=GAMES,
		max_length = CATEGORY_MAX_LEN,
		verbose_name = "Category"
		)
	rating = models.FloatField(
		null=False,
		blank=False,
		max_length = RATING_MAX_LEN
		validators = (MinLengthValidator(RATING_MIN_LEN_AGE),),
		verbose_name = "Rating"
		)
	max_level = models.IntegerField(
		null=True,
		blank=True,
		validators = (MinLengthValidator(MAX_LEVEL_LEN),),
		verbose_name = "Max Level"
		)
	image_url = models.URLField(
		blank=False,
		null=False,
		verbose_name = "Image URL")
	summary = models.TextField(
		null=True,
		blank=True,
		verbose_name = "Summary")





